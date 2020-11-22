# deck_of_cards

Delivered as a python package. 

Install with `pip install -e .`

[Optional] set log level by setting environment variable `DECK_LOG_LEVEL`. Can INFO or DEBUG.

Package has been tested with pytest-bdd for acceptance testing and pytest base for unit testing. Results stored in `tests/`. Install `tests/requirements.txt` to run tests.
To generate coverage report `pytest --cov-report term-missing --cov=deck_of_cards .`

- Requirement: `shuffle()`
Fisher-Yates shuffle algorithm was used here, which takes O(N) time complexity and is performed in place so no additional memory usage. 
- Requirement: `deal_card()`
Deals a card from the end of the list and allows iterating through the deck while dealing avoiding the modify a list while iterating problem that results in skipped items. 
- Deck is poker-style legal
Deck is tested to always initialize a legal deck and after shuffling. 
- Requirement: "Production environment with a lot of usage"
Cards was designed to take up as little memory as possible. Besides those inherited from Object, 2 instance variables are kept in memory, both ints that can be resolved into their associated strings on demand. `SUITS` and `RANKS` are stored as lists as a static variable and accessed by index for O(1) time. This saves memory because, storing rank as 7 instead of "Seven" takes up half the memory and the cost is passed to the access time for the name attributes. Also, assuming `"Seven"` was chosen over `7` as the rank instance var, the dealer would have to waste compute time converting the string for comparison purposes and storing both would take more more memory. 

No Database? Why?
No database was used to store card or deck models. It was assumed that if a round was "interrupted" then the round would need to start over with a new deck. Players never show their cards after a round so no need for historical tracking. Historical tracking would break the rules of poker anyways. Not even our sever admins can cheat! (easily that is...) Logging in DEBUG mode will leak which cards are dealt and the order of the deck post shuffle so don't leave the production server in `DEBUG`. `INFO` level will not leak cards.
Databases add overhead and it was stated this server would see lots of usage. 