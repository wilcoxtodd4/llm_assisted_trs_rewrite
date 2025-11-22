# llm_assisted_trs_rewrite
Rebuilt Tennis Rating System using 98% LLM-aided code

The code in this folder was almost entirely generated using ChatGPT-5.  Most of the prompts have been copied into the repository as well.

About the only things that I didn't use ChatGPT to do were:
  Identify the API connectivity methodologies for tennisreporting.com - I already had those.
  Identify the locations of the data I needed in the JSON files.  Although, after giving it overly detailed instructions for pulling some individual match info, I let it do the rest for gathering set scores, which was probably even more complicated.

Notes from the experience (Round 1):
  This project (in its current state) has taken me about a day.  I still want to go through and add markdown text and other comments, but that should be pretty fast.
  The day it took is way faster than the original creation writing 90% of the code by hand, and then using an older version of ChatGPT to help on specific tasks.
  I'm impressed with the ratings it came up with in step 6.  I will do a full review of the ratings later, but it is definitely spot on for the top players in singles.
  I think I could have been faster by assuming that ChatGPT was more capable than I did.  I typed in a lot of commands related to the JSON layout, which I now think may not have been necessary.
  I need to be less personable - I'm wasting effort being polite.
  What is here seems good, but I definitely need to do more audits.  I had intended to do that and even reminded myself, but something about the flow of getting things done and moving on seems non-conducive to pause for audits.
    This is a major point to remember and to try to change.  This stuff absolutely needs to be audited.
  It's also pretty easy to take a quick look at the results and not do any code review.  I did audit the individual match data cleansing step pretty well, and I had to go back and ask for many changes where my instructions led to misinterpretation.


Notes from the experience (Round 2):
  The initial version from round 1 did not have very much data validation, so that needed to be corrected.  I added a python script called data_quality.py containing a function that can be called to check for duplicates, nulls and whitespace.
  The python code being written as one big chunk is still kind of annoying.  So, I went and broke up some pieces and added some markdowns for commentary.
  I also took the opportunity to have ChatGPT write some rudimentary analysis of the ratings it generated versus the ones that TRS came up with.
    It was quick and easy, but pretty basic, especially the first round (accuracy of TRS vs accuracy of ChatGPT).
    I had it go through and do a little closer look at the places where each model predicted the result incorrectly.
    In most cases, they weren't far off even when they missed.  Tennis results are predictable, but a player favored to win 6-4, 6-4 is only going to win about 85% of the time (from previous testing).
      One match was brutally wrong, and both systems agreed that it should have been a blowout for one player, who lost 2-6, 4-6.  Injury could be a factor.

  One other thing did impress me with ChatGPT.  Even when given vague or incomplete directions, it did pretty well giving me what I wanted.
    I asked for "Both were right" or one of the other was right.  I didn't specify an option for both versions being wrong.  But ChatGPT coded a "Both wrong" option on its own.
    My instructions have been very specific - I'm wondering how far I can loosen them without introducing error.

Overall:  This has been productive and faster than I could have done without ChatGPT, especially since it is in Python.  I still think my SQL coding speed is about the same as prompt entry, but SQL can't score the records easily.
  Commenting is also something that ChatGPT does alright, but since it doesn't know the intent of the instruction, users need to make sure to add that for future users.
  
