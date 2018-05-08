# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

label scene_one:

    #show shana
    sha "Hailey?"
    
    "Glancing up from my phone, {nw}"
    extend "{w=0.3}I see Shana standing in front of me in that beautiful fairy costume.  "
    extend "I grin at her brightly."
    
    #show shana at right with move
    #show hailey at left
    hai "Hey! "
    extend "Ready for makeup?"
    
    
    #show shana smiling
    sha "You bet!"
    hai "Well,{w=0.3} sit down then!"
    
    #show shana
    "She seats herself and removes her glasses,{w=0.3} placing them on the table.  "
    extend "As she does,{w=0.3} I locate Shana's makeup design amongst the other sheets of paper.  "
    
    "Not that I really need it.  "
    extend "\nI practically have this one memorized.  "
    extend "\nIt's easily my favorite and, well..."
    "The fact that it's Shana's definitely helps."
    
    "Turning back to her,{w=0.3} I gently brush some blush onto her foundation-covered cheeks."
    
    hai "Close your eyes,{w=0.3} please."
    "She obediently does as I say,{w=0.3} and I start applying her eyeshadow.  "
    extend "\nOrdinarily it wouldn't take too long but,{w=0.3} well, {nw}"
    extend "{w=0.3}can't a girl take her time so she can spend more time with her crush?"
    
    hai "I can't believe this will be the last time I do this makeup for you.  "
    extend "\nTime sure flies by,{w=0.3} huh?"
    
    sha "It really does,{w=0.3} doesn't it?  "
    extend "The past week has gone by so quickly."
    
    hai "Heh. "
    extend "I swear the dress rehearsal was only yesterday.  "
    extend "\nRemember when you got to put on your costume for the first time?"
    
    sha "I sure do.  "
    extend "\nThough I can hardly remember what it was like when I rehearsed without it now."
    
    hai "All those hours of trying to remember lines..."
    sha "Yeah."  
    
    #show shana concerned
    sha "To be honest,{w=0.3} I’m still worried I’ll miss my entrance cue during Act Two Scene Four again."
    
    menu:
        "Given that she hasn’t missed it during the other performances, I doubt it, but I still want to offer her reassurance."

        "Well the play’s a comedy so, missing your cue could be funnier!":
            $ reassurance = "comedy"
            hai "Well the play’s a comedy so, missing your cue could be funnier!"
            #Shana looks surprised
            "Shana opens her eyes in surprise. Luckily my brush isn’t about to jab her."
            sha "But that makes it worse!"
            sha "Timing in comedy is important!"
            sha "I could mess up the whole moment!"
            hai "I was joking!"
            #Shana looks neutral
            sha "Oh."
            "Well that didn’t turn out the way I had intended."
            "At least her eyeshadow was as good as done anyway."
            hai "Well uh, eyeshadow’s done."

        "You’ve got this, I believe in you!":
            $ reassurance = "gotthis"
            hai "You’ve got this, I believe in you!"
            hai "You know it’s a cue you messed up in rehearsal a lot."
            hai "So I don’t think you’ll forget about it at this stage."
            sha "I hope that’s the case."  
            "She seems a bit more relaxed."
            "I smile and do some final touch ups with her eyeshadow."
            hai "Hmm, you can open your eyes now."
            "She does so, and I admire my handiwork so far."

    
    
    
    
    