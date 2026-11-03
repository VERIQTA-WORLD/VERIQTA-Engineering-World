# Day 6 solution: Write a bounded shell check



## Reasoning and expected result

The script has a narrow positive match and quotes the path. It is a learning contract, not a general configuration parser: duplicate conflicting keys are not rejected, file read errors are collapsed into failure and the file can change after checking. Do not infer production configuration validity from a successful grep.

## Acceptance

Exit codes are 0, 1, 1 and 2 respectively. The valid path contains a space and still passes. Run `sh -n check-config.sh` for syntax evidence separately.

[Return to lesson](../days/day-06.md)
