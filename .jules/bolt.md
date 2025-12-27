## 2025-12-27 - O(n) to O(1) Query Lookups
**Learning:** The application frequently searches for query definitions by name within a list, which is an O(n) operation. As the number of queries grows, this will become a noticeable performance bottleneck.
**Action:** Convert the list of queries (`st.session_state.query_instances`) into a dictionary where the query name is the key. This will change the lookup complexity to O(1), providing a significant performance improvement for query retrieval operations.
