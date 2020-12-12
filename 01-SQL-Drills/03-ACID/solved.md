# ACID


* What are the ACID properties of SQL transactions? If possible, explain each property with an illustration of an example.

Atomicity - meaning all operations inside a transaction take place or none do.

Consistency - this property means if a transaction is completed, all changes will be applied to a database. If there is an error, all changes made will be rolled back (similar to what happens when there is a system failure)

Isolation - every transaction is individual and one transaction can't access the results of other transactions until the transaction is completed.

Durability - once the transaction complete, changes it made to the database will be permanent, even in cases of system failure.