# Django ticket #36143 demo

A demo to simulate the performance improvements in Django ticket #36143.

The ticket aims to use the actual SQL parameters limit set in the SQLite
database, rather than the hardcoded value of 999. This allows bulk queries to be
done in much larger batches, which can significantly reduce the number of
queries.
