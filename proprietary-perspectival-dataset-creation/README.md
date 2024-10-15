Our social media app of choice is Instagram - here is a link to their terms and conditions:
https://help.instagram.com/581066165581870
** PART ONE:

* Step 1: Select a Platform
Instagram
* Step 2: Review Terms of Service & Access Limitations
Instagram allows users to download their data directly through the app. This includes things like photos, comments, and profile details. The step-by-step process of this is in their Help Center under the "Data Download" section.
Instagram doesn't provide straightforward options for bulk data access or an academic API for researchers. If researchers want to access user data for their studies, they usually need to follow the rules set by the API, which can limit the amount and type of data they can use. There may be fees if academic researchers decide to apply for access through the Facebook Graph API.
Researchers can utilize the Instagram Graph API to access some user data, but it is limited to data from accounts that have granted permission.
Earlier, there was a lot more leniency when it came to accessing private data. But ever since data privacy concerns have been circulating and increased regulations such as the General Data Protection Regulation have been put in place, there has been a lot more strictness with how user data is accessed and used.
* Step 3: Document Findings
(on GitHub)
Link to Instagram: https://www.instagram.com/

One big barrier to information from Instagram is the limited amount of posts you can view without an account. After looking at a handful of posts, a pop-up will appear saying that you need to sign in to view more. This can be a large barrier to research and data collection. If you’re trying to use some kind of automated data-scraping program, the necessity of a login/Instagram account might interfere with this.

** PART TWO:



We aimed to collect and analyze data from posts on the official UIUC Instagram account, @illinois1867, focusing on content related to different seasons. For each season, we selected two posts—one photo and one video—to capture a range of media formats. In addition to documenting the content, we created a separate column to record our subjective interpretation of the mood conveyed by each post. To better understand the audience’s engagement, we also tracked key metrics such as the number of likes, comments, and shares. This approach provided us with insights into both the emotional tone of the posts and the interaction levels they generated, helping us explore how seasonal content resonates with viewers across different formats.
Note: For “post type”, a slideshow post and a singular picture post are under the same category (Photo)

**PART THREE:

* Documenting The Data:
Dataset Structure: We captured numerical data such as likes, comments, and shares to quantify engagement with each post. Additionally, we recorded categorical data, including the post link, the season depicted, and whether the content was a picture or video. To add a subjective element to our analysis, we included a personal mood column where we documented our emotional response after interacting with each post.
* Columns:
Post Type, Picture/Video - Categorical
This data is objective, as the distinction between pictures and videos is clearly defined by whether the content involves moving animation or still images. Additionally, the post type is determined by the timestamp, which aligns the content with a specific season, leaving little room for subjective interpretation.
Likes, Comments, Shares - Numerical
All values are present with no missing or null entries, ensuring the dataset is complete.
Reflecting on The Data:
As a group, we approached the task of determining which data to collect from the platform by focusing on metrics that would provide both objective and subjective insights into the posts. We prioritized collecting engagement-related data (likes, comments, shares) to quantify audience interaction and capture categorical data such as the type of post (picture/video) and the season associated with it, as these elements are crucial for understanding content formats and themes.
In terms of difficulties, the main challenge was ensuring that the posts we selected represented the correct season, as some content could be posted out of season but still be related to a particular time of year.
As a group, we decided to create a subjective column to capture the mood each post evoked after interacting with it. This decision came from a desire to complement the objective engagement metrics with a more nuanced, emotional perspective that would allow us to explore how seasonal posts on Instagram affect viewers differently.
While creating this subjective column, we did encounter some discrepancies in how group members interpreted the mood of each post. For instance, a post of autumn trees might evoke feelings of calm and serenity for one person, while another might feel nostalgia or even melancholy. To address these differences, we discussed our individual interpretations in group meetings and agreed on common definitions for the moods we wanted to capture. This helped us bring more consistency to the data, even though each mood remained inherently subjective.
	We came to a consensus that the @illinois1867 would be the most relevant as that is something in common for us all. Analyzing levels of engagement based on season, allowed for a clear distinction to understand how U of I students view and interact with posts on a seasonal basis, and how engagement may fluctuate during the school year and during off-seasons (say: Winter break and Summer break).
	We definitely took into consideration how sponsored posts can falsify engagement or posts that are meant to be shared with friends such as funny posts, memes, or content containing well-known individuals. However, in order to combat this we tried to ensure consistency in our posts and have a deeper focus on nature and the season itself rather than the individuals in the post.
	In creating this dataset, our team took various legal and ethical considerations. Our team chose to analyze posts off of a public Instagram account, specifically because metrics such as likes, shares, etc are visible to the public and do not need to be accessed through an API or an Admin account. The only concern with collecting data in this manner is the aspect of informed consent; the owner of illinois1865 does not know that its posts and its data is being collected for academic research reasons.  
    

