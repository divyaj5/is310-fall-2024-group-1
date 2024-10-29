# Semester Project Midpoint - Data Documentation

For our semester long project, our group aims to explore Flashpoint Archive's collection of Adobe Flash games and focus on the portrayal of women across various dress-up games pre and post-2011. 

### Team Responsibilities
- Project Manager for this Checkpoint: Ellis
- Controlled Vocabulary & Search Methods: A.G. & Divya
- Data Collection: Thea, Ellis, A.G., Divya
    - We each collected 4 games off of the Flashpoint archive, with Ellis & A.G. collecting 8 total games, post-2011, and Divya and Ellis collecting games from pre-2011.
- Documentation Creation: Our documentation is a collective effort between all members of the group, and is updated and revised across various points of the project lifecycle.

## Dataset Overview
This dataset contains multiple variables collected from the chosen games. We collected the name of the game, 
the year it was published, the developer, the publisher, the genders you could choose from, the number of skin tones, 
and a link to the game. Most of that data was to establish context for the game, like what year it was created and who created 
it. The two categories that contained the main data we were trying to gather were gender and number of skin tones, as we were trying 
to track how those numbers changed throughout the years. All of our data was collected from the FlashPoint Archive, and the games that have been collected
currently run on the Ruffle emulator, allowing us to interact with them in-browser. 

### Table Headings
- **game_name**: Name of the Flash game
- **YOR**: Year of Release
- **Operability status**: Current degree of operability within the Ruffle emulator
    - Note: Some games are "partially operable", meaning that the first few sequences in the game are functional, but later on the game will either freeze or restart.
- **Developer**: The user that created the game
    - Our group chose to document the screen name the developer identified themselves by at the time of publishing
- **Publisher**: The platform that published and hosted the game prior to Adobe Flash's retirement
    - Not all games had a listed publisher in the archive. For this reason, some entries are marked N/A.
- **Gender**: The gender options in the dress up game
    - M: Male, F: Female, M/F: Male or Female
- **No. of skintones**: The quantity of skin tone options within the game
- **Game link**: Location of the game within the Flashpoint Archive
    - Our group chose to preserve the game link in case we need to go back for future reference

Additional information: Our group is currently trying to see if it is possible to collect the HEX codes/RGB values of the skin tone palettes
present in each of the games. We are unsure if this is possible with the files that Flashpoint Archive provides its viewers, but in future iterations we aim to collect 
"skin tones" and create a data visualization of the color distributions across games. 

## Sourcing Games: Flashpoint Archive Search
Due to the lack of tabular directories on Flashpoint Archive's API, our group chose to create a controlled vocabulary to utilize the pre-existing search engine on 
the platform. 

## Collecting Data
- (Requirement) Alongside your dataset, you must submit documentation that details the process of data collection and the choices your group made along the way. 
This should include explanations of how you gathered the data, any challenges you encountered, and the criteria you used to include or exclude certain data points. 
You are encouraged to cite readings and materials from class to support your rationale.

### Technologies Used for Data Collection
- **Ruffle Emulator**: Utilized to run and interact with Flash games directly in the browser, facilitating the assessment of customization options and operability.
- **Google Sheets**: Served as the primary platform for collaborative data entry and documentation, allowing team members to simultaneously input and update game data.
- **Web Browser Extensions**: Employed for efficient navigation, screenshot capturing, and data extraction when interacting with the Flashpoint Archive.
- **Version Control (GitHub)**: Managed our documentation and dataset using GitHub, enabling version tracking, collaborative updates, and ensuring that all team members have access to the latest data and documentation.
- **Screen Recording Tools**: Used to capture gameplay sequences, especially for partially operable games, to document and analyze visual elements and customization features.
- **Data Visualization Tools (Planned for Future Iterations)**: Exploring the use of tools like Tableau or Python libraries (e.g., Matplotlib, Seaborn) to create visual representations of skin tone distributions and other collected data.
- **Text Editors/IDEs**: Utilized for any necessary scripting or data manipulation, such as Python or JavaScript, particularly if expanding data collection methods in the future.
- **Cloud Storage Services**: (If applicable) Used for backing up data and ensuring all team members have access to necessary files and resources.
### Summary of Additions
- **Screen Recording Tools**: To capture and analyze gameplay, especially for games that are partially operable.
- **Data Visualization Tools**: Planning to use visualization software for future data analysis and representation.
- **Text Editors/IDEs**: For scripting and data manipulation needs.
- **Cloud Storage Services**: To ensure data backup and accessibility for all team members.

