# 🃏 WHAT IS TWENTY-ONE?
**Twenty-One** is a typical blackjack game project I've worked on for first year college tasks, in which I added a personal sense of personality and thrill! I built upon this program using Visual Studio Code to accomodate the requirements my college expected of me.  
  
## 📦 FEATURES AND TECHNOLOGY
### ╭・TECHNOLOGY
**Twenty-One** was coded using Python 3.11 language using a command-line interface (CLI) to which it has features included but limited to:    
  
### ╭・FEATURES
• Multiple human players competing simultaneously against one dealer;    
• A betting system where players wager each round;  
• A dealer following standard Blackjack rules;  
• Clear display of game states (cards, bets, balances, results);  
• A showing of achievements or titles being earned progressively; and  
• a lot more s-e-c-r-e-t-s to discover...
  
## 🕹️ THE PROCESS
I started by dealing with classes that are particularly foundational in terms of functionality such as Card, Deck, and Hand. These three classes are fundamental to the recurring rounds since methods used in higher classes are heavily based on the methods and attributes under these classes.  

Next, I started working on the Player first. I was contemplating whether I should create a parent class that would occupy both the needs of Player and Dealer class but I went against it since it would add another .py file (I assumed it is not allowed).  

To make sure that I made no mistakes, I intercepted the creation process by going back to the Three Foundational Classes i mentioned earlier. I noticed that my default Ace card value should be 11 instead of 1 from the research I made on other similar games (in Roblox and GTA SA).  

To allow myself freedom, I finally added the main game.py that would allow the five classes to work together. I started with the set-up players to ask_continue methods first, skipping the start method in order to keep myself uncontained in each method functionalities (which worked well).  

When I finished the full functionality, the biggest problem I encountered was creating an engaging gameplay. I fixed the UI first, adding newlines between responses using \n in strings as well as some typo fixes around the code (i.e. numetrical > numerical).  

It hit me afterwards that despite the UI fixes, the game was not entertaining me personally. I added a roleplay system setting the "INSTRUCTIONS" menu to be an introduction by a veteran human gambler and a bunny dealer with respective kakaomoji designs copied from the internet.  

Using this, I was able to create the idea to add delays between responses to create a more "realistic" timing between draw cards, responses, texts, quotes, system updates, and readability of the game.  

This way, I understood that finishing the school project was fine but not doing the best-est I could do would not improve my ability as a student. The funny thing is, now that I am documenting it, the more I realized that I am glad I am pursuing this field to learn more about my skillset that's been always varying since old days.  
  
# 🛠️ DEEP-DIVE
To understand more about this project, I provided flowcharts, class descriptions, method and its parameter descriptions and the problems I encountered and how I dealt with it.  
  
## 🪡 FLOWCHART
<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/4641a236-1bad-4177-8491-8a3b66bae703" />
<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/ba6ee4e5-beb7-48d2-a886-0b25a0481486" />
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/b7951af0-fbbe-4a53-b7c7-e929669de9c4" />
<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/3e1bd76b-206e-4c56-bb58-261b0b009848" />
<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/bf82ae89-a7fc-4e77-ba12-4cfab95d1d53" />
<img width="1920" height="1080" alt="6" src="https://github.com/user-attachments/assets/cf9e8e9c-c43e-4ebe-ae5a-ac25cec607a5" />
<img width="1920" height="1080" alt="7" src="https://github.com/user-attachments/assets/0f0f291f-a262-46df-bd91-d3cadd99a914" />

## 🧐 CLASS DESCRIPTIONS
### Class Card:
This class handles the string representation of each card object along with its respective card value attributes. It can differentiate face cards from value cards along with initializing a default value of 11 for Ace card.  
  
### Class Deck:
This class is responsible for the creation of Card Objects that will be added to a list attribute under this Deck Class. Using the methods under this, it is able to shuffle the card list and deal or draw cards on top of the list.  
  
### Class Hand:
This class is a expected to handle the computation of the total value of each card object that was appended to an innate attribute under this Hand Class. The innate attribute contains an initial empty list that would represent the cards in hand of Players or the Dealer. In addition, using its innate method and attribute, it is able to detect Blackjack and busts. Lastly, similar to Class Card, it is able to handle its string representation.  
  
### Class Player:
This class is handling the main Player data including but not limited to: name, balance, bet, hand, number of wins and losses. Using these attributes, it is able to use a method for placing bets, hit or drawing a card and standing. For additional features, it also features a record result system for achievement based on the number of winds and losses, and a string representation.  
  
### Class Dealer:
This class is handled to follow a fixed rule of hitting until the dealer’s total value card is equal or higher than 17. For additional features, it is able to handle string representation.  
  
### Class BlackjackGame:
This class connects all 5 classes in order to control the flow of the game. It is expected to create a list of players, a Dealer object, a Deck object, and innately handle round number for additional features. To summarize, this class handles setting up the players, starts the bet system, creating deals, running player and dealer turns, deciding the winner, eliminating broke players, continuation of the game, and a full summary of the game per round and at the end of the game.  
  

## 🔃 METHODS USED AND ITS PARAMETERS
### •	Class Card:  
**✻ compute_value(self)**  
This method is designed to determine the value of each Card object depending on the rank attribute.  
  
### •	Class Deck:  
**✻ create_deck(self)**  
This method creates the Card objects which is assigned to the Deck list attribute under Deck class. It runs multiple loops to assign each rank to four respective suits, creating 52 cards in total.  
  
**✻ shuffle(self)**  
This method uses the method: ‘shuffle’ under the random library to randomize the order of the Deck list attributes.  
  
**✻ deal(self)**  
This method is expected to handle empty decks to create new decks and shuffle them. Otherwise, it is also expected to pop the top card on the Deck list attribute representing the ‘hitting’ or ‘drawing’ sequence.  
  
### •	Class Hand:  
**✻ add_card(self, card)**  
This method is responsible for appending the Card object that was/will be popped off the Deck list attribute under Deck class. It uses the card parameter to hold the Card object that’s been popped off the list.  
  
**✻ total(self)**  
This method accesses the protected value attribute under Card class of each objects in order to sum them up. Using a conditional for ace counter and a 21 reference comparator, it is able to decide if the Ace is worth 11 or 1.  
  
**✻ is_bj(self)**  
This method uses its innate method total to test a boolean condition, returning a True value if and only if the total equates to 21 while the number of cards in hand is equal to 2. Otherwise, it returns False.  
  
**✻ is_bust(self)**  
This method uses its innate method total to test a comparator condition, returning a True value if and only if the total is greater than 21  
  
### •	Class Player:  
**✻ place_bet(self, amount)**  
This method uses an input system using the amount parameter. This parameter is tested first against player balance attribute, ensuring that the player is not betting more than their balance or betting 0. This method subtracts the bet from the balance and holds it for use later on.  
  
**✻ hit(self, deck)**  
This method uses the Hand method: ‘add_card’ to handle popped card from the deck, hence its name deck (although I would have preferred it to be card, but according to the PDF given, it was required to be deck).  
  
**✻ stand(self)**  
This method does nothing...  
  
**✻ record_result(self, result)**  
This method is an additional feature that has been added outside the requirements. It records the result based on the parameter result (‘win’, ‘lose’) that will be present later on.  
  
**✻ achievement_title(self)**  
This method uses the innate attribute win count and lose count to handle achievements.  
  
### •	Class Dealer:  
**✻ play_turn(self, deck)**  
This method represents the fixed rules a dealer must follow. It uses the Hand class method: ‘add_card’ to handle drawing cards. It only runs if and only if the dealer total is less than 17.  
  
### •	Class BlackjackGame:  
**✻ start(self)**  
This method controls the flow of the game. It is expected to handle all the methods under BlackjackGame class. At the start, it prints the Round Number. At the end, this class extends its features to printing out summaries of the whole game, and credits.  
  
**✻ setup_players(self)**  
This method handles the player creation processes. It asks the players to input twice: once for the number of players and once for the names of each player. Each sequence of naming will append the names to the list of players attribute under BlackjackGame class. Using logic, it is expected to have input validation against non-integer values for number of players. As an additional feature, it contains a special interaction when the name is ‘admin’.  
  
**✻ place_bets(self)**  
This method is expected to loop and handle the best of each player. It includes an input validation feature and response system for invalid inputs and ‘all-in’ bets. To add, it presents the player balance next to the name per input.  
  
**✻ initial_deal(self)**  
This method is expected to run immediately, dealing with two cards for each player and to the dealer. The method reveals the first card of the dealer, starting the game sequence.  
  
**✻ run_player_turns(self)**  
This method is expected to loop and handle each player. It asks the player for Hit or Stand input using 1 or 2. On the off chance that the player does not input either 1 or 2, it loops by itself with special interactions. If the player chooses to hit, it runs previous method to draw a card, which is also revealed in real time. As an additional feature, this method ends immediately if the player busted, hit 21 exactly or hit blackjack on initial deal.  
  
**✻ run_dealer_turns(self)**  
This method is expected to run immediately after all players are done. First, it reveals the second card of the dealer. Next, this uses the Hand class method: ‘add_card’ to handle drawing cards. It only runs if and only if the dealer total is less than 17. All the drawn cards are revealed in real time.  
  
**✻ resolve_round(self)**  
This method is designed to automate calculations of the results. It decides if the player wins, loses, ties. It is tied to the achievement as well running the record_result method under Player class adding win count or lose count or none at all.   
  
**✻ eliminate_broke_players(self)**  
This method automatically calculates the player balances that are equal to zero, which will then be eliminated. It handles removal of the Player object from the Player list attribute and appendation of it to the Eliminated player list attribute. As an additional feature, it contains a summary of the winning players and an automated response if all players are eliminated.  
  
**✻ ask_continue(self)**  
This method handles the continuation or loop of the game.  
  

## ⛓️‍💥 PROBLEMS ENCOUNTERED + 👷‍♂️ THE MINDSET TO DEAL WITH IT
**✻ Learning the game**  
I was not that familiar with the Blackjack game since I was not exposed to much card games aside from basic Solitaire. In respect to that, I had some troubles regarding what I should use as the default value for the Ace, is it normally 1 or 11. I learned that what I should do is not dwell on the problem but actually research on the functionality. I played a few games on Roblox and GTA SA to learn more about it. In addition, at first, I was confused what ‘dealer fixed rules’ meant, so that was another thing I researched upon.  
  
**✻ Simplifying the for loops**  
Some if not all the loops I made have been a shell of one-liner. To me, it doesn’t look all that pretty because I am not that well-versed in simplifying loops to single lines. All it took was some practice and some testing on what worked and what did not.  
  
**✻ Forgetting the requirements and rules of Blackjack**  
This problem is another lack of knowledge on my part and some key misunderstandings that delayed my code. At first, I could not create the blackjack checker because I thought blackjack means it must be 21 with 2 OR more cards. I was able to deal with it through more research and re-checking my code using the PDF instructions as a guideline.  
  
**✻ How payout system works**  
My first prototype was not able to subtract the balances properly and through it, it was able to cheat its way and duplicate balances. By adding proper safety measures and subtracting the bet from the balance in placing bets step, I was able to deal with this problem and other related issues that arose.  
  
**✻ Forgetting () in calling the methods**  
The more common issue I’ve had with dealing with OOP is the lack of experience I had of it. With respect to that, I was not familiar at all with the habit of adding a parenthesis to call my methods to which it was more often than not, forgotten to be added in the methods creating a chain of errors. I dealt with it with patience and using try-except debugging solutions.  
  
**✻ UI and Readability**  
The biggest issue with the final prototype I made was that the computer responses are completely INSTANT. It is not bad for a code but for a game, it is. I solved it by adding delays using time library and sleep method I searched up online. This also gave me the idea to create a role play setting in this game. Using these, I was able to deal with both readability and UI issues I’ve had with blackjack.  
  
  
# 🗒️ INSTRUCTIONS
## HOW TO RUN THIS PROJECT?
1. Install all the py files in this repository.
2. Install and Run Visual Studio Code.
3. Put all the py files in one folder and open it from VS Code.
4. Run the main.py file using **Ctrl + R** or Run the Terminal.
5. Enjoy the game.
  
## VIDEO
https://github.com/user-attachments/assets/693ef28b-b08c-4c86-a07e-7ba61a4cb95b
  
## CREDITS
### ╭・[cute symbols for crds](https://docs.google.com/document/d/173Z3L5sbzuvLIa4CWRvOmx20Hy00zPYhfBxm0DVxBTA/edit?tab=t.0)
• This docs was a great help in designing the role-play setting giving a sense of realism to my work!
  
