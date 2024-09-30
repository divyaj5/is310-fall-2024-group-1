# Instructor Feedback on Initial IS310 Project Proposal

Overall, I think you have a strong foundation for your semester-long project. Your proposed focus on Adobe Flash games is both relevant and creative, and I particularly appreciate your coining of “customization-themed” games as a way to explore the evolution of Flash games before their decommissioning in 2020. This focus, along with your interest in analyzing the portrayal of gender in these games, is well-aligned with the course objectives. I also really like the idea of combining web scraping of metadata with actually playing these games to investigate your chosen themes in depth.

Your rotation of the Project Manager role and thoughtful acknowledgment of each group member’s expertise shows a strong start in organizing your collaboration. Additionally, your timeline provides a solid framework for moving forward.

However, there are several areas that need further development to ensure your project remains feasible and successful:

- **Clarifying Patterns & Plans for Augmenting the Dataset:** While you mention exploring the evolution of graphics and portrayals of gender, the “patterns” you’re looking to analyze remain vague. Are you examining visual trends (e.g., color palettes, character design, or stylistic changes) or gameplay mechanics? Similarly, how do you plan to assess gender portrayal? Clarifying these patterns and developing a coding framework for them will help give your analysis more structure and depth. Without this specificity, your project risks becoming too broad so I would encourage you to consider these categories more closely. Furthermore, the assignment requires you to augment any pre-existing datasets in a meaningful way. So, how will you add new layers of data, such as your coding of aesthetic or thematic patterns? You might also consider what data to include for games that are no longer operational. For example, rather than excluding non operational games, you might consider including data about the degree of operability of each game in your dataset.
  
- **Assessing Metadata & Documentation:** The assignment emphasizes the importance of understanding and documenting how cultural objects are transformed into data. While you’ve identified the Flashpoint Archive as your primary data source, you’ll need to critically assess how the archived metadata was created. For example, how reliable and comprehensive is the tagging or categorization of these games? I do think you'll be able to web scrape the metadata, though if you actually inspect each game in the browser you'll notice that the data is actually available as a json object like this one from the game you included in your proposal, [https://db-api.unstable.life/search?id=21ed7be1-1eac-4b62-adb6-0a88ae1fa2ac&limit=1](https://db-api.unstable.life/search?id=21ed7be1-1eac-4b62-adb6-0a88ae1fa2ac&limit=1) that you could use instead of web scraping. This returns the following data:

```json
[
  {
    "id": "21ed7be1-1eac-4b62-adb6-0a88ae1fa2ac",
    "library": "arcade",
    "title": "Duck Life 2: World Champion",
    "alternateTitles": "DuckLife 2: World Champion",
    "series": "Duck Life",
    "developer": "Wix",
    "publisher": "Bubblebox",
    "source": "https://www.kongregate.com/games/wixgames/ducklife2-world-champion",
    "tags": [
      "Simulation",
      "Avian",
      "Auto-zipped"
    ],
    "platform": "Flash",
    "playMode": "Single Player",
    "status": "Playable",
    "version": "",
    "releaseDate": "2010-07-13",
    "language": "en",
    "notes": "",
    "originalDescription": "The sequel to the duck training sim. Travel the globe racing your duck to become the world champion.\nHope you all like it!\nI’m starting a new website called Wix Games so if you see any of my future games made by them, then you know it’s me :)",
    "dateAdded": "2018-04-18T05:21:29.864Z",
    "dateModified": "2024-03-29T17:37:10.440845Z",
    "applicationPath": "FPSoftware\\Flash\\flashplayer_32_sa.exe",
    "launchCommand": "http://localflash/ducklife2b.swf",
    "zipped": true
  }
]
```

You'll notice the `source` field, which could be a useful way to start to assess the validity of the metadata. You'll also notice `tags`, which could be useful for assessing how consistent archivists have been in applying these vocabularies and whether there are any gaps or biases in the data. Relatedly, you’ve identified some key limitations of working with the Flashpoint Archive, such as issues with search functionality and needing to create keywords for searching. I think this is a smart approach but you might also explore the Flashpoint Archive wiki and documentation more in-depth to inform your understanding of the search filters and whether there's even controlled vocabularies that you could use. I've also quickly found this guide form the FlashPoint Archive Wiki [https://flashpointarchive.org/datahub/Searching_the_Collection](https://flashpointarchive.org/datahub/Searching_the_Collection) which seems to provide the full master list of games in a tabular format, so curious if you had seen this yet and if you plan to use it.

- **Division of Labor & Timeline:** As I mentioned previously, you’ve done a good job outlining each member’s expertise and the plan for rotating the Project Manager role. However, I think you need much more detail to ensure the project's success going forward. For example, I believe one member of the group has since dropped the course, so how will that impact the proposed division of labor and distribution of tasks? Also you haven't really detailed who will do what exactly? Are you planning all to do the same tasks simultaneously, or are you planning to leverage each member's expertise and assign them tasks relevant to their interests? I would also recommend thinking more in-depth about how many games you want to test locally and how many you need to develop and test your full dataset collection and curation workflow. I recommend starting with a subset of data, since you can always add additional data once you have a clear protocol in place. But eventually you will need to consider how much data is sufficient to achieve your project goals. To help with that assessment, I would highly recommend starting to identify existing relevant scholarship on the history of Flash games to help contextualize and inform your analysis and datasets. Finally, your timeline ends on October 29th but you'll notice that you still have a number of project milestones to complete after that date, so I would recommend returning to the full project description (available here [https://cultureasdata-uiuc.github.io/is310-fall-2024/assessments/03-semester-project](https://cultureasdata-uiuc.github.io/is310-fall-2024/assessments/03-semester-project)) to further refine your timeline and division of labor.

Again overall, this is a very strong start to your project, and I’m excited to see how you develop your research proposal further. I think you have a lot of potential to create a really interesting and innovative project that will contribute to our understanding of Flash games and internet subcultures. If you have any questions or need further guidance, please don’t hesitate to reach out. Great work so far!