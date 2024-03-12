**Developed a full-fledged online auction platform using Django.**

Implemented functionalities for:

* User Management: Registration, login, and logout with user authentication.
* Auction Listings:
    * Model creation for storing details like title, description, starting bid, optional image URL, and category.
    * Functionality for users to create and edit new listings with the aforementioned details.
* Active Listings Page: Displays a list of all currently active auctions showcasing title, description, current price, and photo (if available).
* Individual Listing Page: Provides detailed information about a specific listing, including:
    * Current price and bidding functionality (users can place bids meeting specific criteria).
    * Watchlist management (signed-in users can add/remove listings from their watchlist).
    * Ability for the listing creator to close the auction, declaring the winner.
    * Commenting system for signed-in users to add comments to the listing.
* Your Biddings and Your Listings Pages: For the user to track items he has listed or has bid on 
* Watchlist: Dedicated page displaying all listings a user has added to their watchlist.
* Category System:
    * Implemented category models and functionality.
    * Users can browse a list of all categories and view active listings within each category.
* Django Admin Interface:
    * Provided comprehensive administrative access for viewing, adding, editing, and deleting listings, comments, and bids.
