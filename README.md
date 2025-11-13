# llm_assisted_trs_rewrite
Rebuilt Tennis Rating System using 98% LLM-aided code

The code in this folder was almost entirely generated using ChatGPT-5.  Most of the prompts have been copied into the repository as well.

About the only things that I didn't use ChatGPT to do were:
  Identify the API connectivity methodologies for tennisreporting.com - I already had those.
  Identify the locations of the data I needed in the JSON files.  Although, after giving it overly detailed instructions for pulling some individual match info, I let it do the rest for gathering set scores, which was probably even more complicated.

Notes from the experience:
  This project (in its current state) has taken me about a day.  I still want to go through and add markdown text and other comments, but that should be pretty fast.
  The day it took is way faster than the original creation writing 90% of the code by hand, and then using an older version of ChatGPT to help on specific tasks.
  I'm impressed with the ratings it came up with in step 6.  I will do a full review of the ratings later, but it is definitely spot on for the top players in singles.
  I think I could have been faster by assuming that ChatGPT was more capable than I did.  I typed in a lot of commands related to the JSON layout, which I now think may not have been necessary.
  I need to be less personable - I'm wasting effort being polite.
  What is here seems good, but I definitely need to do more audits.  I had intended to do that and even reminded myself, but something about the flow of getting things done and moving on seems non-conducive to pause for audits.
    This is a major point to remember and to try to change.  This stuff absolutely needs to be audited.
  It's also pretty easy to take a quick look at the results and not do any code review.  I did audit the individual match data cleansing step pretty well, and I had to go back and ask for many changes where my instructions led to misinterpretation.
