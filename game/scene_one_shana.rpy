# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

label scene_one_shana:

    play music "audio/dont have a cue s1 shana.mp3"

    scene dressing room two with fade:
    show hailey artist sheepish blush with dissolve
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

    show hailey artist frown with dissolve
    hai "I knew were acting oblivious,{w=0.3} but I assumed you were just playing hard to get.  "
    extend "I didn't realize you actually didn't know."
    hai "Most people would have gotten the message."

    show hailey artist frown:
        ease 0.6 xpos 0.8 ypos 1.0

    show dressing room two:
        ease 0.6 xalign 0.2 yalign 0.5

    "I avoid eye contact out of embarrassment."
    sha "I get comments like that a lot.  "
    extend "I misread people all the time."
    extend "\nI'm kind of slow when it comes to interpreting nonverbal cues."
    "Since Hailey asked me out,{w=0.3} I figure that this would be the best time to tell her."
    "I also somehow feel like I can trust her."

    show hailey artist frown:
        ease 0.6 xpos 0.5 ypos 1.0

    show dressing room two:
        ease 0.6 xalign 0.5 yalign 0.5

    sha "Can I tell you a secret?"
    hai "Sure.  "
    extend "Share away."

    show hailey artist frown:
        ease 0.6 xpos 0.2 ypos 1.2

    show dressing room two:
        ease 0.6 xalign 0.8 yalign 0.2

    "I look away again to avoid eye contact."
    sha "Do you promise that you won't judge me for it?"

    show hailey artist frown:
        ease 0.6 xpos 0.5 ypos 1.0

    show dressing room two:
        ease 0.6 xalign 0.5 yalign 0.5

    show hailey artist surprised with dissolve
    "I notice that Hailey's eyes widen.  "
    extend "I think she looks a little taken aback."

    show hailey artist determined with dissolve
    hai "I won't judge.  "
    extend "What is it?"

    show hailey artist frown:
        ease 0.6 xpos 0.6 ypos 1.2

    show dressing room two:
        ease 0.6 xalign 0.4 yalign 0.2

    "I look away again."

    show hailey artist surprised with dissolve
    sha "I'm on the autism spectrum."
    sha "It's sometimes hard for me to pick up on subtle social cues."

    show hailey artist thoughtful with dissolve
    sha "Especially nonverbal ones."
    hai "Wow...{w=0.5} I wouldn't have identified it myself,{w=0.3} but that makes a lot of sense in context."

    show hailey artist neutral with dissolve
    hai "Is that why you usually get squeamish when people apply your makeup?"

    show hailey artist frown:
        ease 0.6 xpos 0.5 ypos 1.0

    show dressing room two:
        ease 0.6 xalign 0.5 yalign 0.5

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

            show hailey artist neutral with dissolve
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

            show hailey artist frown:
                ease 0.6 xpos 0.2 ypos 1.0

            show dressing room two:
                ease 0.6 xalign 0.8 yalign 0.5

            sha "I'm sorry for sending mixed signals."
            sha "Reading people is something I try to improve on constantly."

            show hailey artist insistent with dissolve
            hai "Don't apologize!"

            show hailey artist frown:
                ease 0.6 xpos 0.5 ypos 1.0

            show dressing room two:
                ease 0.6 xalign 0.5 yalign 0.5

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

label scene_one_shana_part_four:

    play music "audio/dont have a cue s1 cafe.mp3"

    scene black with dissolve

    "I feel a little nervous as I walk to the café."
    "I’ve never been good at making small talk."
    "I briefly consider stalling,{w=0.3} but I decide against it."
    "I wouldn’t want to be rude on a first date."

    scene cafe with dissolve:
        xalign 0.1 yalign 0.5

    "As I enter the café,{w=0.3} I see that Hailey is already there."

    show hailey date neutral with dissolve
    sha "Hailey!"
    sha "You look really cute in your outfit."
    sha "Shall we order?"

    show hailey date upset with dissolve
    hai "Hello to you too."
    sha "Huh?"

    show hailey date frown with dissolve
    hai "People usually greet each other when they see them."
    sha "I did greet you though."
    sha "I got your attention by calling your name."
    sha "I didn’t think I needed to say ‘hello’ after you had already seen me."

    show hailey date surprised with dissolve
    hai "I hadn’t thought about that."
    hai "That makes a lot of sense."

    show hailey date sheepish with dissolve
    hai "Sorry for overreacting."
    sha "No problem!"

    show hailey date happy with dissolve
    hai "Want to order now?"
    sha "Sure!"
    hai "Since I asked you out on the date,{w=0.3} I can pay for both of us this time."
    sha "Are you sure?"
    sha "I don’t want to inconvenience you."
    hai "I insist!"
    sha "Thank you.  "
    extend "I’ll accept your offer."
    sha "I’ll have an iced coffee,{w=0.3} black."
    hai "Oh wow...{w=0.3} I always have to have my coffee with a ton of cream and sugar."
    sha "I used to be the same way."
    sha "I got used to black coffee after enough all-nighters though."

    hide hailey with dissolve
    show cafe:
        ease 0.6 xalign 0.5 yalign 0.5
    "After getting our drinks,{w=0.3} we take our seats."

    show hailey date happy with dissolve
    hai "How are you today?"
    hai "Have you gotten to rest now that the show is over?"
    sha "I feel great!"
    sha "And yes!  "
    extend "I’ve been sleeping a lot."
    sha "I’m a little sad though that the theater productions are all over for this semester."
    sha "I’m excited to perform again next semester though."
    sha "Do you think you’ll do makeup again?"

    show hailey date upset with dissolve
    hai "About that..."
    hai "I have something I need to tell you."
    hai "I really didn’t want to start the conversation with this."
    hai "But I guess it would have come up eventually."
    sha "You can share anything with me."

    show hailey date nervous with dissolve
    hai "I guess I’ll just say it."
    hai "I’m considering changing fields."
    sha "That’s nothing to be ashamed of!"
    sha "A ton of students change their major during college."
    sha "I have friends who changed their major more than once."
    hai "I’m not thinking about changing my major."
    sha "Then what are you thinking about?"
    hai "I’ve never been that good of a student.  "
    extend "Even in high school."
    hai "Being in college has made me realize that I don’t think academia is for me."
    hai "I’m considering dropping out and going to trade school."
    sha "Oh,{w=0.3} wow."
    sha "I wasn’t expecting you to say that."
    sha "What type of trade?"

    show hailey date nervous blush with dissolve
    hai "My first thought was cosmetology."
    sha "That makes sense given your interest in makeup art."
    sha "Even if you’re going to beauty school,{w=0.3} we can still see each other often though!"
    sha "I’m sure there must be schools nearby."

    show hailey date sad with dissolve
    hai "I don’t think you understand."
    hai "I can’t go to beauty school here."
    hai "I’m only in this town for college."
    hai "If I dropped out,{w=0.3} I’d have to move back home."
    sha "Why?"
    hai "Right now,{w=0.3} my student loans are helping me pay for my housing."
    hai "When I drop out I won’t have those anymore."
    hai "And on top of that,{w=0.3} I’d have to start paying them back."
    sha "That makes sense..."
    sha "How far away is your house?"
    hai "It’s about a two hour flight."
    sha "Oh.  "
    extend "That kind of sucks."
    sha "That’s not that far though!"
    sha "We could still visit each other sometimes."
    sha "We also have our phones and computers."

    show hailey date sadsmile with dissolve
    hai "That’s true!"
    sha "You also haven’t moved yet."
    sha "Let’s get to know each other better while you’re still here."
    hai "Good idea!"

    "There’s a moment of silence as we think of a new conversation topic."
    "I hate small talk."
    "I feel relieved when Hailey talks first."

    show hailey date happy with dissolve
    hai "Enough about me."
    hai "I want to know more about you."
    hai "I don’t think you’ve even told me your major."
    sha "I’m majoring in literature with a minor in theater."

    show hailey date surprised with dissolve
    sha "I love all forms of storytelling."

    hai "I know I shouldn’t be surprised because of how good you are at acting."
    hai "For some reason I pegged you as more of a science person."

    show hailey date sly with dissolve
    hai "I could just be biased though because my current major is biochemistry."

    show hailey date happy with dissolve
    sha "A lot of people assume that."
    sha "I’m decent at math and science,{w=0.3} but my main passion is language arts."

    show hailey date confused with dissolve
    hai "Why is that?"
    sha "When I was younger,{w=0.3} I got frustrated a lot when I misread people and when they misread me."
    sha "I gravitated towards books because I could interpret them in any way I wanted to."
    sha "When I read written words,{w=0.3} there’s also no chance of me missing social subtleties."

    show hailey date happy with dissolve
    hai "That makes sense."
    hai "What about theater then?"
    hai "If you don’t mind sharing,{w=0.3} is it difficult for you to get into character?"
    hai "Obviously it’s hard for anyone,{w=0.3} but I can imagine that it might be harder for someone who has trouble reading emotions."
    sha "I don’t mind at all!"
    sha "I don’t find it hard."
    sha "I think I actually have more practical experience with acting than most people."

    show hailey date confused with dissolve
    hai "How so?"
    sha "I have to act all the time."

    show hailey date frown with dissolve
    sha "When I was younger,{w=0.3} I got harassed a lot for using the wrong facial expression."
    sha "Or for using the wrong tone."
    sha "Or for not making eye contact when people expected me to."
    sha "I think theater is a pretty natural transition for me."

    show hailey date neutral with dissolve
    hai "What type of career do you want to do after college?"

    show hailey date neutral:
        ease 0.6 xpos 0.3 ypos 1.1

    show cafe:
        ease 0.6 xalign 0.7 yalign 0.1

    sha "I’d love to be a professional actress."
    sha "I don’t know if that’s a realistic career goal though."

    show hailey date neutral:
        ease 0.6 xpos 0.5 ypos 1.0

    show cafe:
        ease 0.6 xalign 0.5 yalign 0.5

    show hailey date happy with dissolve
    hai "If that’s what you want,{w=0.3} you should go for it!"
    hai "Would you want to continue acting in plays?"
    sha "I do love theater."
    sha "But if I could do anything,{w=0.3} I would want to act for movies."

    show hailey date surprised with dissolve
    sha "Acting for camera allows a lot more room for subtleties."

    show hailey date wink with dissolve
    hai "Well,{w=0.3} if you do become a movie star,{w=0.3} I can say I knew you before it was cool."

    show hailey date wink:
        ease 0.6 xpos 0.6 ypos 1.2

    show cafe:
        ease 0.6 xalign 0.4 yalign 0.2

    sha "You could."

    show hailey date happy with dissolve

    hai "So, what type of movies would you want to act in?"
    hai "I can see you in a comedy!"

    show hailey date happy:
        ease 0.6 xpos 0.5 ypos 1.0

    show cafe:
        ease 0.6 xalign 0.5 yalign 0.5

    sha "I like trying out different types of roles."
    sha "If I could I’d love to be in a horror film."

    show hailey date surprised with dissolve
    hai "Oh wow..."

    show hailey date sheepish with dissolve
    hai "I’m not the biggest horror fan."
    sha "Really? Why not?"
    hai "I’m too easily spooked I guess."
    hai "I’ve never liked jump scares."
    hai "And I have a low tolerance for gore."

    menu:
        "It bothers me as a literature student that Hailey has such a one-dimensional view of horror as a genre."

        "I decide to inform Hailey about how broad the horror genre can be.":

            show hailey date nervous with dissolve
            sha "Horror is so much more than jump scares and gore!"

            show hailey date surprised with dissolve
            sha "They’re definitely a large part of some sub-genres,{w=0.3} but many horror films don’t use gore or jump scares at all."
            sha "Many horror films use atmospheric and psychological techniques to be scary."

            show hailey date recoil with dissolve
            jump scene_one_shana_part_five

        "I decide to drop the subject.":
            sha "If you don’t watch horror,{w=0.3} what type of movies do you like then?"
            jump scene_one_shana_part_six

label scene_one_shana_part_five:
    menu:
        "Hailey doesn’t look like she’s sure how to respond."

        "I decide to continue.":
            sha "Horror movies also allow for some of the most inventive artistic choices that you wouldn’t see in more ‘realistic’ genres."
            sha "Considering that you’re a makeup artist,{w=0.3} I’m surprised you don’t like horror movies."

            show hailey date sheepish with dissolve
            hai "I do appreciate gore makeup a lot."
            hai "I’d love to learn more about how to apply it."

            show hailey date insistent with dissolve
            hai "I don’t like watching gory movies though."
            sha "That’s fair."
            sha "What type of movies do you like watching then?"

        "I decide to drop the subject.":
            sha "I got a bit carried away there."
            sha "Sorry about that."

            show hailey date happy with dissolve
            hai "It’s okay."
            sha "If you don’t watch horror,{w=0.3} what type of movies do you like then?"


label scene_one_shana_part_six:

    show hailey date excited with dissolve
    hai "Mostly action."
    hai "I’ve been loving the superhero movies coming out lately."
    sha "I love superheroes!"
    sha "What draws you to superhero movies?"
    hai "I like that they’re fast paced."

    show hailey date sly with dissolve
    hai "Movies these days are so long, I zone out during a lot of them."

    show hailey date excited with dissolve
    hai "I can usually pay attention to superhero movies though."
    hai "I also like that they’re gratifying."
    hai "When you watch a superhero movie,{w=0.3} you go in kind of knowing that the hero will win,{w=0.3} you know?"
    sha "I get what you mean."
    sha "You definitely don’t expect that when you watch a horror movie."
    sha "Who’s your favorite superhero?"

    show hailey date thoughtful with dissolve
    hai "There are so many!  "
    extend "It’s hard to pick just one."
    hai "If I had to choose..."

    show hailey date sheepish blush with dissolve
    hai "I’d say I have a soft spot for Poison Ivy and Harley Quinn’s relationship."

    show hailey date frown with dissolve
    sha "That doesn’t count!"
    sha "They’re not even superheroes!"
    sha "They’re villains."

    show hailey date insistent with dissolve
    hai "They still have superpowers though!"
    hai "I think they should count."

    show hailey date sly with dissolve
    hai "Besides, there’s no clear line between heroism and villainy."

    show hailey date happy with dissolve
    hai "Poison Ivy commits a lot of her crimes to protect nature."
    "I drop the point."
    sha "That’s fair."
    sha "I do love their relationship too!"

    "Once we got over our initial nerves,{w=0.3} the conversation flowed naturally."
    "The rest of the date went well."
