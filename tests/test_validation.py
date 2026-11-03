"""Positive and adversarial tests for repository validation."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('validator',Path(__file__).parents[1]/'scripts/validate.py')
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

class MetadataTests(unittest.TestCase):
    def setUp(self):
        import json
        self.good=json.loads((v.ROOT/'catalogue/library.json').read_text())[0]
    def test_valid_record(self):
        self.assertEqual(v.record_errors([self.good]),[])
    def test_missing_metadata(self):
        x=copy.deepcopy(self.good); del x['environment']
        self.assertTrue(any('missing metadata' in e for e in v.record_errors([x])))
    def test_duplicate_ids(self):
        self.assertTrue(any('duplicate ID' in e for e in v.record_errors([self.good,self.good])))
    def test_invalid_reference(self):
        x=copy.deepcopy(self.good); x['prerequisites']=['UNKNOWN']
        self.assertTrue(any('invalid prerequisite' in e for e in v.record_errors([x])))
    def test_review_requires_evidence(self):
        x=copy.deepcopy(self.good); x['status']='reviewed'
        self.assertTrue(any('reviewed without' in e for e in v.record_errors([x])))
    def test_execution_requires_evidence(self):
        x=copy.deepcopy(self.good); x['execution']['status']='passed'
        self.assertTrue(any('execution evidence' in e for e in v.record_errors([x])))
    def test_planned_path_rejected(self):
        x=copy.deepcopy(self.good); x['status']='planned'
        self.assertTrue(any('planned item has' in e for e in v.record_errors([x])))
    def test_boolean_minutes_rejected(self):
        x=copy.deepcopy(self.good); x['estimated_minutes']=True
        self.assertTrue(any('invalid estimated time' in e for e in v.record_errors([x])))

class MarkdownTests(unittest.TestCase):
    def check(self,text,other='# Other\n\n## Target\n'):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); p=root/'page.md'; p.write_text(text)
            (root/'other.md').write_text(other)
            return v.markdown_errors(root,p)
    def test_valid_link_anchor(self):
        self.assertEqual(self.check('# Page\n\n[Go](other.md#target)\n'),[])
    def test_missing_file(self):
        self.assertTrue(any('missing link' in e for e in self.check('# Page\n\n[Go](missing.md)\n')))
    def test_invalid_anchor(self):
        self.assertTrue(any('broken anchor' in e for e in self.check('# Page\n\n[Go](other.md#missing)\n')))
    def test_code_fixture_link_ignored(self):
        self.assertEqual(self.check('# Page\n\n```text\n[fiction](absent.md)\n```\n'),[])
    def test_html_image_checked(self):
        errors=self.check('# Page\n\n<img src="absent.svg">\n')
        self.assertTrue(any('missing link' in e for e in errors))
        self.assertTrue(any('lacks alt' in e for e in errors))
    def test_repository_escape(self):
        self.assertTrue(any('escapes repository' in e for e in self.check('# Page\n\n[Go](../outside.md)\n')))
    def test_heading_and_whitespace(self):
        errors=self.check('# Page\n\n### Skipped  \n')
        self.assertTrue(any('skipped' in e for e in errors))
        self.assertTrue(any('trailing' in e for e in errors))
    def test_duplicate_heading_slugs(self):
        self.assertEqual(v.headings('# Title\n\n## Test\n\n## Test\n'),{'title','test','test-1'})

class RepositoryInvariantTests(unittest.TestCase):
    def test_repository_static_checks_pass(self):
        self.assertEqual(v.validate(), [])

    def test_missing_required_section_is_rejected(self):
        import shutil
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'repo'
            shutil.copytree(v.ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
            page=root/'library/vw-e001.md'
            page.write_text(page.read_text().replace('## Cleanup','## Removed heading'))
            self.assertTrue(any('missing sections' in e and 'VW-E001' in e for e in v.validate(root)))

    def test_invalid_cross_catalogue_reference_is_rejected(self):
        import shutil
        import json
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'repo'
            shutil.copytree(v.ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
            p=root/'catalogue/journey.json'
            records=json.loads(p.read_text());records[0]['related_library']=['VW-NOPE']
            p.write_text(json.dumps(records))
            self.assertTrue(any('invalid library reference' in e for e in v.validate(root)))

class SectionValidationTests(unittest.TestCase):
    def setUp(self):
        import json
        self.records=json.loads((v.ROOT/'catalogue/sections.json').read_text())
        self.ids={'VW-DAY001','VW-DAY002','VW-DAY003','VW-C001','VW-E007','VW-I006'}

    def test_valid_sections(self):
        self.assertEqual(v.section_errors(v.ROOT,self.records,self.ids),[])

    def test_invalid_content_reference(self):
        self.records[0]['content_ids'].append('VW-UNKNOWN')
        self.assertTrue(any('invalid section content reference' in e for e in v.section_errors(v.ROOT,self.records,self.ids)))

    def test_planned_section_cannot_claim_authored_page(self):
        self.records[1]['path']='foundations/engineering-evidence/README.md'
        self.assertTrue(any('planned section claims' in e for e in v.section_errors(v.ROOT,self.records,self.ids)))

    def test_ready_section_needs_validation_record(self):
        self.records[0]['publication_state']='ready'
        self.records[0]['validation']='missing.md'
        self.assertTrue(any('missing section validation' in e for e in v.section_errors(v.ROOT,self.records,self.ids)))

    def test_reviewed_section_needs_independent_reviewer(self):
        self.records[0]['status']='reviewed'
        self.assertTrue(any('section review lacks evidence' in e for e in v.section_errors(v.ROOT,self.records,self.ids)))

if __name__=='__main__':
    unittest.main()
