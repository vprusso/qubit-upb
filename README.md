# upb

**Question**: *In what dimensions do there exist qubit unextendible product bases (UPBs)?*

## Usage

The `upb` package requires [`uv`](https://docs.astral.sh/uv/) to be installed. Once installed, you can run the following command:

```bash
uv run python main.py
```

## Summary of UPBs

# Classification of Qubit Unextendible Product Bases

Columns p=1 through p=8 are **fully resolved**. The only open cases are in p=9 (8 unknown entries).

| Size | p=1 | p=2 | p=3 | p=4 | p=5 | p=6 | p=7 | p=8 | p=9 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 1 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 2 | :white_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 3 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 4 | :x: | :white_check_mark: | :white_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: |
| 5 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 6 | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :x: | :x: | :x: | :x: |
| 7 | :x: | :x: | :x: | :white_check_mark: | :x: | :x: | :x: | :x: | :x: |
| 8 | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :x: | :x: |
| 9 | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :x: | :x: | :x: |
| 10 | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: [^7] | :white_check_mark: [^1] | :x: | :white_check_mark: [^6] |
| 11 | :x: | :x: | :x: | :x: | :white_check_mark: [^7] | :white_check_mark: [^7] | :white_check_mark: [^4] | :white_check_mark: [^6] | :x: |
| 12 | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 13 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: [^7] | :white_check_mark: [^7] | :white_check_mark: | :question: |
| 14 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: [^7] | :white_check_mark: | :question: |
| 15 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: [^7] | :white_check_mark: | :question: |
| 16 | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 17-18 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :question: |
| 19 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: [^7] | :white_check_mark: | :question: |
| 20-21 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :question: |
| 22-26 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 27 | :x: | :x: | :x: | :x: | :x: [^2] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 28 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 29-31 | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 32 | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 33-58 | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 59 | :x: | :x: | :x: | :x: | :x: | :x: [^2] | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 60 | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 61-63 | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 64 | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 65-122 | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 123 | :x: | :x: | :x: | :x: | :x: | :x: | :x: [^2] | :white_check_mark: | :white_check_mark: |
| 124 | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 125-127 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: |
| 128 | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 129-250 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: |
| 251 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: [^2] | :white_check_mark: |
| 252 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: |
| 253-255 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 256 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: |
| 257-506 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 507 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: [^2] |
| 508 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 509-511 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 512 | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |

Entries without footnotes were established by Johnston [[3]](#ref3). A :white_check_mark: indicates a UPB of the given size exists, :x: indicates no such UPB exists, and :question: indicates existence is unknown.

## References

<a id="ref1"></a>[1] Wang, Kai, and Lin Chen. ["The construction of 7-qubit unextendible product bases of size ten."](https://link.springer.com/article/10.1007/s11128-020-02684-8) Quantum Information Processing 19 (2020): 1-17.

<a id="ref2"></a>[2] Chen, Lin, and Dragomir Z. Djokovic. ["Nonexistence of n-qubit unextendible product bases of size 2^n-5."](https://link.springer.com/article/10.1007/s11128-017-1791-8) Quantum Information Processing 17 (2018): 1-10.

<a id="ref3"></a>[3] Johnston, Nathaniel. ["The structure of qubit unextendible product bases."](https://iopscience.iop.org/article/10.1088/1751-8113/47/42/424034) Journal of Physics A: Mathematical and Theoretical 47.42 (2014): 424034.

<a id="ref4"></a>[4] Sun, Yize and Chen, Lin. ["The construction and local distinguishability of multiqubit unextendible product bases."](https://arxiv.org/abs/2102.11553) arXiv:2102.11553 (2021).

<a id="ref5"></a>[5] Bennett, Charles H., et al. ["Unextendible product bases and bound entanglement."](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.82.5385) Physical Review Letters 82.26 (1999): 5385-5388.

<a id="ref6"></a>[6] Johnston, Nathaniel. ["The minimum size of qubit unextendible product bases."](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TQC.2013.93) Proceedings of TQC 2013, LIPIcs 22 (2013): 93-105.

<a id="ref7"></a>[7] Chen, Lin, and Dragomir Z. Djokovic. ["Multiqubit UPB: The method of formally orthogonal matrices."](https://doi.org/10.1088/1751-8121/aac53b) Journal of Physics A 51.26 (2018): 265302.

[^1]: Wang and Chen (2020)
[^2]: Chen and Djokovic, nonexistence (2018)
[^4]: Sun and Chen (2021)
[^6]: Johnston (2013)
[^7]: Chen and Djokovic, formally orthogonal matrices (2018)

