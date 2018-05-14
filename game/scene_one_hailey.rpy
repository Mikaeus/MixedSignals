# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

label scene_one_hailey:

    play music "audio/dont have a cue s1 hailey.mp3"

    scene black

    sha "Hailey?"

    scene dressing room one with fade
    show shana fairy neutral with dissolve

    "Glancing up from my phone, {nw}"
    extend "{w=0.3}I see Shana standing in front of me in that beautiful fairy costume.  "
    extend "I grin at her brightly."

    hai "Hey! "
    extend "Ready for makeup?"

    show shana fairy slightsmile with dissolve
    sha "You bet!"
    hai "Well,{w=0.3} sit down then!"

    show shana fairy neutral noglasses with dissolve
    "She seats herself and removes her glasses,{w=0.3} placing them on the table.  "
    extend "As she does,{w=0.3} I locate Shana's makeup design amongst the other sheets of paper.  "

    "Not that I really need it.  "
    extend "I practically have this one memorized.  "
    extend "It's easily my favorite and, well..."
    "The fact that it's Shana's definitely helps."

    show shana fairy neutral noglasses blush with dissolve
    "Turning back to her,{w=0.3} I gently brush some blush onto her foundation-covered cheeks."

    hai "Close your eyes,{w=0.3} please."

    show shana fairy closedeyes noglasses blush with dissolve
    "She obediently does as I say,{w=0.3} and I start applying her eyeshadow.  "
    extend "\nOrdinarily it wouldn't take too long but,{w=0.3} well, {nw}"
    extend "{w=0.3}can't a girl take her time so she can spend more time with her crush?"

    show shana fairy closedeyes noglasses eyeshadow with dissolve
    hai "I can't believe this will be the last time I do this makeup for you.  "
    extend "\nTime sure flies by,{w=0.3} huh?"

    sha "It really does,{w=0.3} doesn't it?  "
    extend "The past week has gone by so quickly."

    hai "Heh. "
    extend "I swear the dress rehearsal was only yesterday.  "
    extend "\nRemember when you got to put on your costume for the first time?"

    sha "I sure do.  "
    extend "Though I can hardly remember what it was like when I rehearsed without it now."

    hai "All those hours of trying to remember lines..."
    sha "Yeah."

    show shana fairy concerned closedeyes noglasses eyeshadow with dissolve
    sha "To be honest,{w=0.3} I'm still worried I'll miss my entrance cue during Act Two Scene Four again."

    menu:
        "Given that she hasn't missed it during the other performances,{w=0.3} I doubt it,{w=0.3} but I still want to offer her reassurance."

        "Well the play's a comedy, so missing your cue could be funnier!":
            $ reassurance = "comedy"
            hai "Well the play's a comedy,{w=0.3} so missing your cue could be funnier!"

            show shana fairy surprised noglasses eyeshadow with dissolve
            "Shana opens her eyes in surprise."
            extend "\nLuckily,{w=0.3} my brush isn't about to jab her."
            sha "But that makes it worse!"
            sha "Timing in comedy is important!"
            extend "\nI could mess up the whole moment!"
            hai "I was joking!"

            show shana fairy neutral noglasses eyeshadow with dissolve
            sha "Oh."
            "Well that didn't turn out the way I had intended."
            "At least her eyeshadow was as good as done anyway."
            hai "Well,{w=0.3} uh...{w=0.5} eyeshadow's done."

        "You've got this, I believe in you!":
            $ reassurance = "gotthis"
            hai "You've got this,{w=0.3} I believe in you!"
            hai "You know it's a cue you messed up in rehearsal a lot.  "
            extend "\nSo I don't think you'll forget about it at this stage."

            show shana fairy closedeyes noglasses eyeshadow with dissolve
            sha "I hope that's the case."
            "She seems a bit more relaxed."
            "I smile and do some final touch ups with her eyeshadow."
            hai "Hmm,{w=0.3} you can open your eyes now."

            show shana fairy neutral noglasses eyeshadow with dissolve
            "She does so,{w=0.3} and I admire my handiwork so far."

label scene_one_hailey_part_two:
    "She looks past me at the mirror,{w=0.3} and gazes at herself."

    sha "It looks so beautiful."
    hai "Beautiful makeup for a beautiful girl."
    sha "The detail is amazing."
    hai "You say that as if this is the first time I've done it."
    sha "Well,{w=0.3} all of the other times don't make this time less pretty!"
    hai "Fair enough,{w=0.3} fair enough."

    "Time for the eyeliner."
    hai "Look down please."

    show shana fairy eyesdown noglasses eyeshadow with dissolve
    "Once she does so,{w=0.3} I gently reach forward with the eyeliner pencil and apply it to her top lids."
    "I still remember the time she practically jumped out of her chair,{w=0.3} when someone tried doing this last production."
    "So,{w=0.3} given how still she is with me,{w=0.3} I always feel special."

    hai "Now look up."

    show shana fairy eyesup noglasses eyeshadow with dissolve
    "I repeat the process with her bottom eyelids."
    "As I step away,{w=0.3} she relaxes."
    "Because she wears glasses,{w=0.3} mascara isn't really needed,{w=0.3} and she's already applied her lipstick.  "
    extend "Which means I only have one thing to do left."

    hai "Close your eyes again?"

    show shana fairy closedeyes noglasses eyeshadow with dissolve
    "Selecting the right brush,{w=0.3} I start to paint decorations across her eyelids and down one of her cheeks."

    hai "Did you know this is my favourite part?"
    sha "Really?"
    hai "I get to decorate your pretty face with these pretty designs."
    sha "I suppose for you this must be fun."
    sha "The sensation of the brush down my cheek always feels strange."
    hai "In a good way?"
    sha "I wouldn't say it's good or bad.  "
    extend "Just not what I'm used to."
    hai "Fair enough!"

    show shana fairy closedeyes noglasses decorations with dissolve
    "Stepping back,{w=0.3} I admire the full effect of her makeup,{w=0.3} and, well...{w=0.5} her face in general."
    "Satisfied,{w=0.3} I nod and grin."
    hai "There,{w=0.3} done!"

    show shana fairy happy noglasses decorations with dissolve
    sha "Thanks!"

    show shana fairy happy decorations with dissolve
    "I hand over her glasses,{w=0.3} and she places them back on."
    "She stands up and looks at herself in the mirror,{w=0.3} smiling."
    "I can't help but smile as well."
    "It might seem silly,{w=0.3} but It's great just being able to be in the same space as her."
    "Sadly,{w=0.3} another one of the leads is already standing there,{w=0.3} looking at me expectantly."
    sha "I guess I'll be going then."
    sha "Thanks again Hailey."
    hai "Of course!  "
    extend "\nBreak a leg!"

    hide shana with dissolve
    "I wave her goodbye and turn my attention to the other lead."


    "Between light conversation with the remaining leads,{w=0.3} and just generally doing my job,{w=0.3} the next half an hour passes by quickly."
    "Soon,{w=0.3} all of the actors have departed to do warm ups down on the stage,{w=0.3} leaving me and the rest of the crew to our own devices."
    "I figure I might as well get some study in,{w=0.3} but I always find myself scrolling on my phone again."
    "Not that there's anything interesting going on there either."
    "Just as I wonder if boredom will force me to look through my book,{w=0.3} most of the actors come backstage again."
    "Not Shana of course.  "
    extend "Since she's a lead,{w=0.3} she has to be side stage already."
    "She only gets a break during intermission."
    "She must be so exhausted by now."
    "Soon enough,{w=0.3} the play begins."

    show dressing room one:
        ease 0.6 xalign 0.9 yalign 0.1

    "A TV provides everyone in the dressing room a live broadcast of the stage."
    "Not only does that allow the actors to know when they need to get ready,{w=0.3} but It also gives me an alternative to studying."
    "I feel like I've seen it a million times now,{w=0.3} but it's still stunning."
    "It's impressive how much talent is in this college."
    "Shame I can't really say the same amount myself."
    "Besides my makeup skills,{w=0.3} I'm a pretty average student."
    "Given how much of a high achiever I was in high school,{w=0.3} no one is more disappointed in me that I am."
    "Sometimes I think about whether I should drop out of my course and go to Beauty School or something."
    "Intermission starts,{w=0.3} and all of the actors are back."

    show dressing room one:
        ease 0.6 xalign 0.5 yalign 0.5

    "I see Shana in the corner,{w=0.3} staring at her script.  "
    extend "She's no doubt trying to remember her cue."

    if reassurance == "comedy":
        "I hope my earlier comment about missing her cue isn't making her panic more."
    else:
        "Hopefully my words of encouragement earlier make her feel better about it."

    menu:
        "Should I go over to her?"

        "No, I shouldn't bother her.":
            $ botherShana = "dontBother"
            "As much as I want to talk to her,{w=0.3} she seems pretty focused."

        "Why not?":
            $ botherShana = "whyNot"
            "There's no reason not to,{w=0.3} right?"
            "I stride on over to her corner of the room."
            hai "Hey!"

            show shana fairy surprised decorations with dissolve
            "She nearly drops her script in surprise."

            show shana fairy irritated decorations with dissolve
            sha "Hailey not now."
            "Realising she wants to be left alone,{w=0.3} I mutter an apology and retreat back to where I was sitting."

            hide shana with dissolve

label scene_one_hailey_part_three:

    "Intermission ends soon after that."

    show dressing room one:
        ease 0.6 xalign 0.9 yalign 0.1

    "Act Two is when things get interesting, so I find myself staring at the TV for the whole time."
    "Much to my relief,{w=0.3} Shana doesn't miss that cue,{w=0.3} and her entrance is met with plenty of laughter."
    "As the scenes go by,{w=0.3} the fact that this will all be over soon finally sinks in."
    "Given that I didn't exactly donate hours and hours of time for rehearsing like the actors,{w=0.3} this wouldn't matter too much to me."
    "But I had planned to do something once it finished: asking Shana out on a date."
    "Usually I'm pretty bold when asking out girls I like but,{w=0.3} she's been giving me mixed signals at best."
    "She hasn't downright turned me down though,{w=0.3} so I've been under the assumption she's playing hard to get."
    "I've definitely been too obvious for her to be unaware of my feelings towards her."
    "Still,{w=0.3} I don't know what her response will be."
    "I'm so not used to not knowing!"
    "Before I know it,{w=0.3} it's the final scene,{w=0.3} and then curtain call."
    "When Shana walks up to the front of the stage for her bow,{w=0.3} I give her a little clap of my own."

    show dressing room one:
        ease 0.6 xalign 0.1 yalign 0.5

    "A few minutes later,{w=0.3} the actors all come stampeding in,{w=0.3} whooping and cheering."
    "I spot her as soon as she walks through the door."

    hai "Shana!"

    show shana fairy happy decorations with dissolve
    "She smiles as she races towards me."
    "I embrace her gleefully. She wraps her arms around me."

    hide shana with dissolve
    hai "You did it!"
    "She laughs."
    sha "We all did it!"

    show shana fairy sideglance decorations with dissolve
    "I pull away and look at her."

    "Damn, she's not even looking back at me."
    "Maybe this was a mistake."
    "I take a deep breath."
    hai "We should continue seeing each other outside of all of this production stuff."
    sha "I'd like that."
    hai "You know,{w=0.3} just the two of us."
    "I look at her suggestively but she doesn't seem like she's getting the hint."
    hai "Like...{w=0.3} a date."
