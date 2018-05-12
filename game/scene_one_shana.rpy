# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

label scene_one_shana:
    
    "I looked at Hailey in disbelief."
    "I usually only interact with Hailey during productions,{w=0.3} but I've still known her for about two years now."
    "I never would have guessed that she liked me.  "
    extend "I try to think back to cues she might have given in the past."
    "Thinking back on it,{w=0.3} Hailey has complimented me on my appearance a lot."
    "I tend to be straightforward when expressing opinions myself though,{w=0.3} so I never thought anything of it."
    "She also winks at me a lot,{w=0.3} which has always been a gesture I've had a hard time interpreting."
    "I try to remember if I've ever seen her wink at anyone else."
    sha "Wow.  " 
    extend "I wasn't expecting you to do that."
    
    show hailey artist confused with dissolve
    hai "Seriously?  "
    extend "I've been dropping hints for months now." 
    sha "Like what?"
    hai "Like uh...{w=0.5} winking at you!  "
    extend "I only really do that when I'm flirting with someone."
    
    show hailey artist sheepish blush with dissolve
    hai "Oh and,{w=0.3} to be honest,{w=0.3} sometimes I kind of stalled when applying your makeup so that we'd be together longer."
    hai "I usually talk to people a bit when I do their makeup,{w=0.3} but not as much as I do with you."
    
    show hailey artist thoughtful with dissolve
    hai "Did you really not notice?"
    sha "I didn't."
    hai "I knew were acting oblivious,{w=0.3} but I assumed you were just playing hard to get.  "
    extend "I didn't realize you actually didn't know." 
    hai "Most people would have gotten the message."
    
    #Shana looks away (Hailey sprite moves out of focus. Background moves?)
    "I avoid eye contact out of embarrassment."
    sha "I get comments like that a lot.  "
    extend "I misread people all the time."
    extend "\nI'm kind of slow when it comes to interpreting nonverbal cues."
    "Since Hailey asked me out,{w=0.3} I figure that this would be the best time to tell her."
    "I also somehow feel like I can trust her."
    
    #Shana looks towards Hailey again.
    sha "Can I tell you a secret?"
    hai "Sure.  "
    extend "Share away."
    
    #Shana looks away
    "I look away again to avoid eye contact."
    sha "Do you promise that you won't judge me for it?"
    
    #Shana looks towards Hailey again.
    show hailey artist surprised with dissolve
    "I notice that Hailey's eyes widen.  "
    extend "I think she looks a little taken aback."
    
    show hailey artist determined with dissolve
    hai "I won't judge.  " 
    extend "What is it?"
    
    #Shana looks away
    "I look away again."
    
    show hailey artist surprised with dissolve
    sha "I'm on the autism spectrum."
    sha "It's sometimes hard for me to pick up on subtle social cues."
    
    show hailey artist thoughtful with dissolve
    sha "Especially nonverbal ones."
    hai "Wow...{w=0.5} I wouldn't have identified it myself,{w=0.3} but that makes a lot of sense in context."
    
    show hailey artist neutral with dissolve
    hai "Is that why you usually get squeamish when people apply your makeup?"
    sha "Yeah.  "
    extend "I don't like being touched very much."
    sha "It's a lot easier for me to deal with when you're the one applying it though!"
    sha "I feel comfortable around you."
    
    show hailey artist happy with dissolve
    hai "I'll take that as a compliment."
    "I feel unsure if Hailey still wants to go out with me now."
    
    menu:
        "So far she seems to be taking it well,{w=0.3} but some people have reacted badly upon finding out about my diagnosis."

        "I think I should ask for clarification.":
            sha "Do you still want to go out with me,{w=0.3} even after hearing all that?"
            
            show hailey artist frown with dissolve
            hai "Why do you ask?"
            hai "Do I seem like someone who wouldn't be okay with it?"
            sha "Of course not!"
            sha "I'm sorry for even asking."
            sha "I've just gotten bad reactions from other people in the past."
            sha "I just wanted clarification."
            
            show hailey artist insistent with dissolve
            hai "Of course I still do."
            sha "I'd love to go out with you then."
         
        "I think it's safe to assume she still wants to date me.":
            sha "I'd love to go out with you."

            show hailey artist surprised with dissolve
            hai "Seriously?"
            hai "Wow...{w=0.5} I wasn't expecting you to actually say yes."
            hai "You've been sending mixed signals."
            hai "Like sometimes avoiding eye contact." 
            hai "And brushing off my compliments."
            hai "But it makes sense in context now."

label scene_one_shana_part_two:
        
    menu:
        "I know I shouldn't, but I feel bad about unintentionally brushing Hailey off."

        "I think I should apologize.":
            #Shana avoids eye contact
            sha "I'm sorry for sending mixed signals."
            sha "Reading people is something I try to improve on constantly."
            
            show hailey artist insistent with dissolve
            hai "Don't apologize!"
            
            #Shana makes eye contact
            show hailey artist upset with dissolve
            hai "Is there anything I can do to help?"
         
        "I think I should explain my communication style.":
            sha "I tend to interpret things pretty literally." 
            
label scene_one_shana_part_three:

    sha "It helps a lot when people are clear with me about their intentions." 
    sha "Though...{w=0.5} I can see how that would ruin some of the fun of flirting."
    
    show hailey artist happy with dissolve
    hai "No problem!"
    hai "Now that I know,{w=0.3} I'll be more straightforward." 
    hai "When are you free?"
    sha "I'll have free time this weekend now that the play is over."
    hai "Do you want to go on a date this weekend then?"
    sha "Sure!  "
    extend "Where do you want to go?"
    hai "Want to grab coffee together at a cafe?"
    
    show hailey artist laugh with dissolve
    hai "I'm kind of broke at the moment."
    
    menu: 
        "I feel like making a sarcastic retort, but I hesitate."

        "I make the joke.":
            sha "Really?  "
            extend "The other students I know have tons of money."
            
            show hailey artist upset with dissolve
            hai "Those people are lucky then."
            sha "I meant that sarcastically."
            hai "Oh!  " 
            extend "My bad."
            
            show hailey artist happy with dissolve
            hai "You're right.  "
            extend "I don't know anyone who's broke." 
         
        "I abandon the joke.":
            sha "I am too.  " 
            extend "I think most college students are."

            show hailey artist happy with dissolve
            hai "So is a coffee date fine with you?"
            sha "Sure!  "
            extend "I'm excited for it."


