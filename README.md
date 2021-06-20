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

![summary](https://user-images.githubusercontent.com/74985818/122660163-1af6c900-d14d-11eb-84db-fa10d6d060ba.png)

- How many Vine reviews and non-Vine reviews were there?
  - Total Vine reviews = 12
  - Total non-Vine reviews = 30,029
- How many Vine reviews were 5 stars? How many non-Vine reviews were 5 stars?
  - Total Vine reviews with 5 Stars = 4
  - Total non-Vine reviews with 5 Stars = 14,511
- What percentage of Vine reviews were 5 stars? What percentage of non-Vine reviews were 5 stars?
  - Total reviews = 30,029
  - Percentage of vine reviews = 0.013%
  - Percentage of non-Vine reviews = 48.303%

# SUMMARY:
- From the above results we can see that of the total 5 star reviews, only 0.01% are from vine program and 48.30% reviews are not from Vine program. So there is no bias in the data.
- One other way of analyzing this data is to consider all reviews and not filter the data with 5 star ratings, since all reviews are considered while making a purchase.
