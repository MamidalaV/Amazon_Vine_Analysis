# Amazon_Vine_Analysis

# PURPOSE:
## The purpose of this analysis is to analyze Amazon reviews written by members of the paid Amazon Vine program. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review.

# RESULTS
The following dataset is used for this analysis, which is csv file with reviews about Mobiles and Electronics.

![dataset](https://user-images.githubusercontent.com/74985818/122659786-47104b00-d149-11eb-8007-4b64450af03b.png)

This dataset is filtered to get the columns to match the table in pgAdmin.

![table](https://user-images.githubusercontent.com/74985818/122659818-ad956900-d149-11eb-81c3-b5d6c23ac00a.png)

Products with more than 20 reviews are filtered.

![morethan20](https://user-images.githubusercontent.com/74985818/122659837-cef65500-d149-11eb-8fc6-0746cda1eef8.png)

Using the 'helpful_votes' and 'total_votes' columns, a percentage is derived and only reviews with 50% or more helpful have been filtered.

![morethan50perc](https://user-images.githubusercontent.com/74985818/122659867-06fd9800-d14a-11eb-9967-32f31d04d508.png)

Under the Amazon vine program, since the customers get products for free to review, reviews from these customers are filtered using vine == 'Y'

![paid](https://user-images.githubusercontent.com/74985818/122659896-56dc5f00-d14a-11eb-9a83-f30a21bc2447.png)

Also the unpaid reviews (not in vine program) are filtered, using vine == 'N'

![unpaid](https://user-images.githubusercontent.com/74985818/122659905-69569880-d14a-11eb-8638-0227b81b7b5d.png)

Finally to analyze the reviews, the above subsets of the data are used to create a summary.

![summary](https://user-images.githubusercontent.com/74985818/122659911-84c1a380-d14a-11eb-9d86-f8aea3c23ade.png)



# SUMMARY:
