# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

label scene_one_hailey:

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
    sha "To be honest,{w=0.3} I’m still worried I’ll miss my entrance cue during Act Two Scene Four again."
    
    menu:
        "Given that she hasn’t missed it during the other performances,{w=0.3} I doubt it,{w=0.3} but I still want to offer her reassurance."

        "Well the play’s a comedy, so missing your cue could be funnier!":
            $ reassurance = "comedy"
            hai "Well the play’s a comedy,{w=0.3} so missing your cue could be funnier!"
            
            show shana fairy surprised noglasses eyeshadow with dissolve
            "Shana opens her eyes in surprise."
            extend "\nLuckily,{w=0.3} my brush isn’t about to jab her."
            sha "But that makes it worse!"
            sha "Timing in comedy is important!"
            extend "\nI could mess up the whole moment!"
            hai "I was joking!"
            
            show shana fairy neutral noglasses eyeshadow with dissolve
            sha "Oh."
            "Well that didn’t turn out the way I had intended."
            "At least her eyeshadow was as good as done anyway."
            hai "Well,{w=0.3} uh...{w=0.5} eyeshadow’s done."

        "You’ve got this, I believe in you!":
            $ reassurance = "gotthis"
            hai "You’ve got this,{w=0.3} I believe in you!"
            hai "You know it’s a cue you messed up in rehearsal a lot.  "
            extend "\nSo I don’t think you’ll forget about it at this stage."
            
            show shana fairy closedeyes noglasses eyeshadow with dissolve
            sha "I hope that’s the case."  
            "She seems a bit more relaxed."
            "I smile and do some final touch ups with her eyeshadow."
            hai "Hmm,{w=0.3} you can open your eyes now."
            
            show shana fairy neutral noglasses eyeshadow with dissolve
            "She does so,{w=0.3} and I admire my handiwork so far."

    
    
    
    
    