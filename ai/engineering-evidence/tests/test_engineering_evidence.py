"""Test the learning measurement contract, including misleading edge cases."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('evidence',ROOT/'ai/engineering-evidence/examples/check_evidence.py')
e=importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
HEADER=','.join(e.FIELDS)+'\n'


class EvidenceTests(unittest.TestCase):
    def measure(self, rows):
        return e.summarise(io.StringIO(HEADER+rows))

    def test_fixture_matches_independently_written_totals(self):
        with (ROOT/'ai/engineering-evidence/examples/requests.csv').open(newline='') as stream:
            actual=e.summarise(stream)
        expected=json.loads((ROOT/'ai/engineering-evidence/examples/expected.json').read_text())
        self.assertEqual(actual,expected)

    def test_inclusive_limit_and_fast_wrong_result(self):
        x=self.measure('A,baseline,/search,200,true,500\nB,baseline,/search,200,true,501\nC,baseline,/search,200,false,1\n')
        self.assertEqual(x['baseline']['demonstrated_good'],1)
        self.assertEqual(x['baseline']['status_200'],3)

    def test_unknown_stays_in_denominator(self):
        x=self.measure('A,candidate,/search,200,unknown,1\n')
        self.assertEqual(x['candidate']['eligible'],1)
        self.assertEqual(x['candidate']['demonstrated_good'],0)
        self.assertEqual(x['candidate']['unknown_correctness'],1)

    def test_health_checks_cannot_improve_search_fraction(self):
        x=self.measure('A,baseline,/health,200,true,1\nB,baseline,/search,503,false,2\n')
        self.assertEqual(x['baseline']['eligible'],1)
        self.assertEqual(x['baseline']['good_fraction'],0)

    def test_no_search_traffic_is_unknown(self):
        x=self.measure('A,baseline,/health,200,true,1\n')
        self.assertIsNone(x['baseline']['good_fraction'])
        self.assertIsNone(x['candidate']['good_fraction'])

    def test_duplicate_id_rejected(self):
        with self.assertRaises(ValueError):
            self.measure('A,baseline,/search,200,true,1\nA,candidate,/search,200,true,1\n')

    def test_bad_columns_rejected(self):
        with self.assertRaises(ValueError):
            e.summarise(io.StringIO('id,result\nA,true\n'))

    def test_invalid_and_incomplete_values_rejected(self):
        for row in ['A,other,/search,200,true,1','A,baseline,/other,200,true,1',
                    'A,baseline,/search,999,true,1','A,baseline,/search,200,yes,1',
                    'A,baseline,/search,200,true,-1','A,baseline,/search,200,true,1,extra',
                    'A,baseline,/search,200,true','A,baseline,/search,200,true,1.2']:
            with self.subTest(row=row), self.assertRaises(ValueError):
                self.measure(row+'\n')

    def test_cli_reads_fixture_without_writing(self):
        output=io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(e.main([str(ROOT/'ai/engineering-evidence/examples/requests.csv')]),0)
        self.assertEqual(json.loads(output.getvalue())['baseline']['eligible'],12)

    def test_cli_errors_return_two_without_input_dump(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'invalid.csv';p.write_text('PRIVATE_SENTINEL\n')
            for args in [[],[str(p)], [str(Path(d)/'missing.csv')]]:
                out,err=io.StringIO(),io.StringIO()
                with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                    self.assertEqual(e.main(args),2)
                self.assertNotIn('PRIVATE_SENTINEL',out.getvalue()+err.getvalue())


if __name__=='__main__':
    unittest.main()
