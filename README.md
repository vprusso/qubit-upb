# qubit-upb

**Question**: *In what dimensions do there exist qubit unextendible product bases (UPBs)?*

A set $\mathcal{S} = \\{\ket{\psi_1}, \ldots, \ket{\psi_n}\\} \subset (\mathbb{C}^2)^{\otimes p}$ is an *unextendible product basis* (UPB) of size $n$ on $p$ qubits if:

1. Each $\ket{\psi_i}$ is a product state: $\ket{\psi_j} = \ket{\phi_j^{(1)}},
   \otimes \cdots \otimes \ket{\phi_j^{(p)}}$ where $\ket{\phi_j^{(i)}} \in
\mathbb{C}^2$ for each qubit $i$.

2. The states are mutually orthogonal: $\langle \psi_{j_1} | \psi_{j_2} \rangle
   = 0$ for all $j_1 \neq j_2$.

3. The set is unextendible: there is no product state $\ket{\psi} \in
   (\mathbb{C}^2)^{\otimes p}$ such that $\langle \psi | \psi_j \rangle = 0$ for
all $j \in \{1, \ldots, n\}$. 


# Classification of Qubit Unextendible Product Bases

Columns p=1 through p=8 are **fully resolved**. The only open cases are in p=9 (8 unknown entries: s=13, 14, 15, 17, 18, 19, 20, 21).

| Size | p=1 | p=2 | p=3 | p=4 | p=5 | p=6 | p=7 | p=8 | p=9 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 1 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^6][^7] | ❌[^6] |
| 2 | ✅[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^6][^7] | ❌[^6] |
| 3 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^6][^7] | ❌[^6] |
| 4 | ❌[^3] | ✅[^3] | ✅[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^6][^7] | ❌[^6] |
| 5 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^6][^7] | ❌[^6] |
| 6 | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ❌[^3] | ❌[^3] | ❌[^6][^7] | ❌[^6] |
| 7 | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^6][^7] | ❌[^6] |
| 8 | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ❌[^6][^7] | ❌[^6] |
| 9 | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ❌[^3] | ❌[^6][^7] | ❌[^6] |
| 10 | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^7] | ✅[^1] | ❌[^6][^7] | ✅[^6] |
| 11 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^7] | ✅[^7] | ✅[^4] | ✅[^6] | ❌[^3] |
| 12 | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 13 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^7] | ✅[^7] | ✅[^6][^7] | ❓ |
| 14 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^7] | ✅[^6][^7] | ❓ |
| 15 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^7] | ✅[^6][^7] | ❓ |
| 16 | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 17-18 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ❓ |
| 19 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^7] | ✅[^6][^7] | ❓ |
| 20-21 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ❓ |
| 22-26 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 27 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^2] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 28 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 29-31 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 32 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 33-58 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 59 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^2] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 60 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 61-63 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 64 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 65-122 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 123 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^2] | ✅[^6][^7] | ✅[^3] |
| 124 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 125-127 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^6][^7] | ✅[^3] |
| 128 | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ❌[^3] | ✅[^3] | ✅[^6][^7] | ✅[^3] |
| 129-250 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅[^6][^7] | ✅[^3] |
| 251 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌[^2] | ✅[^3] |
| 252 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅[^6][^7] | ✅[^3] |
| 253-255 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌[^6][^7] | ✅[^3] |
| 256 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅[^6][^7] | ✅[^3] |
| 257-506 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅[^3] |
| 507 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌[^2] |
| 508 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅[^3] |
| 509-511 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌[^3] |
| 512 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅[^3] |

A ✅ indicates a UPB of the given size exists, ❌ indicates no such UPB exists, and ❓ indicates existence is unknown. Cells for sizes exceeding 2^p are ❌ trivially (size exceeds Hilbert space dimension).

## References

[^1]: Wang, Kai, and Lin Chen. ["The construction of 7-qubit unextendible product bases of size ten."](https://link.springer.com/article/10.1007/s11128-020-02684-8) Quantum Information Processing 19 (2020): 1-17.

[^2]: Chen, Lin, and Dragomir Z. Djokovic. ["Nonexistence of n-qubit unextendible product bases of size 2^n-5."](https://link.springer.com/article/10.1007/s11128-017-1791-8) Quantum Information Processing 17 (2018): 1-10.

[^3]: Johnston, Nathaniel. ["The structure of qubit unextendible product bases."](https://iopscience.iop.org/article/10.1088/1751-8113/47/42/424034) Journal of Physics A: Mathematical and Theoretical 47.42 (2014): 424034.

[^4]: Sun, Yize and Chen, Lin. ["The construction and local distinguishability of multiqubit unextendible product bases."](https://arxiv.org/abs/2102.11553) arXiv:2102.11553 (2021).

[^5]: Bennett, Charles H., et al. ["Unextendible product bases and bound entanglement."](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.82.5385) Physical Review Letters 82.26 (1999): 5385-5388.

[^6]: Johnston, Nathaniel. ["The minimum size of qubit unextendible product bases."](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TQC.2013.93) Proceedings of TQC 2013, LIPIcs 22 (2013): 93-105.

[^7]: Chen, Lin, and Dragomir Z. Djokovic. ["Multiqubit UPB: The method of formally orthogonal matrices."](https://doi.org/10.1088/1751-8121/aac53b) Journal of Physics A 51.26 (2018): 265302.

