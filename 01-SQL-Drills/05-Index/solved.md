# Index

## Part 1

* Explain an index in SQL.

Indexes in SQL are identifiers used to locate specif rows.

## Part 2

* What are the different types of `index`? If possible, explain each type with an illustration.

B-tree indexes allow searches, insertion, deletions, and sequential access (ex: used with operators like =, BETWEEN, IS NULL, etc.)

Hash indexes only handle equality comparison.

Gin indexes are generalized inverted indexes, which are useful when there are multiple stored values within a column.

BRIN indexes are blocked range indexes. These are used on columns with linear sort orders.

GiST (Generalized Search Tree) indexes allow building of general tre stuctures. They are used in indexing geometric data types and full-text search. SP-GiST indexes are useful for data that has natural clustering and is not an equally balanced tree.

