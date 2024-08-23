Summary
The main e-commerce website experienced a significant slowdown, with page load times increasing from 2 seconds to over 15 seconds.

Timeline:
10:00 AM: Issue detected via monitoring alert indicating elevated response times on the checkout page.
10:05 AM: Initial investigation by the on-call engineer suggested a possible issue with the web server’s load balancing.
10:15 AM: Further investigation ruled out load balancing issues; focus shifted to the database as the potential bottleneck.
10:30 AM: A misleading path led to tweaking the application server configurations, which had no effect on performance.
11:00 AM: Escalated to the database team after noticing increased query execution times.
11:15 AM: Database logs analyzed, revealing that several queries were taking excessively long to complete.
11:45 AM: Identified the root cause as a missing index on a frequently accessed table in the database.
12:00 PM: Database team added the missing index and optimized the affected queries.
12:15 PM: System performance returned to normal; monitoring confirmed stability.
12:30 PM: Incident officially marked as resolved.

Root Cause and Resolution:
Root Cause: 
The database query optimization process had failed to create an index on a table that had recently been expanded with additional columns. This resulted in full table scans for queries that should have been using an index, overwhelming the database server as traffic increased.
Resolution: 
The database team created the missing index and optimized the affected queries to ensure they were using the correct indexes. This immediately improved query performance, reducing page load times back to normal levels.
