Building purplexity - the sister of perplexity. How is it different, it allows the user to generate a matplotlib animation styled explanation of the entire search


So user query -> validation + auth -> vector search (similarity + confidence score calculation) -> if(cs<0.5 send to tavily) else if (cs>0.5 and cs<0.9) vector + tavily, else share to letta -> Tavily to letta -> letta to server -> db transaction -> client


things to cache - 1) user queries 2) responses 

