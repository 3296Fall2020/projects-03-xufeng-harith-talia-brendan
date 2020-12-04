# Knock-Knock

## Project Overview
This repository is for Temple CIS 3296 Group Project Assignment. 
The goal of this project is to train a AI model for home-security cameras to identify visitors at front door, save the record with times, and sent notifications if needed. The software will stream the video from the security camera as input, analyze and identify visitor with trained model. The software will generate result base on the result given by the model and write it to the log file for tracking purposes. For example, it will record a carrier from UPS stopped by at 10:12am, and a carrier from USPS came to drop a package at 14:25pm. 

The main objects to identify includes:
1. Amazon delivery-man
2. UPS delivery-man
3. Fedex delivery-man
4. USPS postman
5. Pizza delivery-man
6. Package thief (if possible)

## Vision Statement
For residents or small companies/organizations, who need a way to keep track of received packages for security and organizational purposes, the Knock Knock application is an excellent surveillance system that allows its users to keep an eye on who is delivering packages at their door. Unlike the average security camera system, such as Ring, Knock Knock uses Artificial Intelligence to decipher what kind of delivery-man is at your door-step. Our product will allow users to be notified of when someone is at your door, first determining whether or not they are dropping off a package, as well as which company they are delivering from.

## User Personas
### Harith
Dylan, age 27, is a Financial Manager in a large investment firm in Malvern, PA with over 17,000 employees. He is originally from Boston, where he went to Harvard University to obtain a bachelor’s degree in Economics. He is back and forth between Malvern and Boston as he normally visits home at least once a month. He is single and lives with a friend in an apartment near work and hopes to continue his career in the greater Philadelphia area, for now, ultimately moving on to the DMV areas in the future. He initially started his career as a Financial Advisor, taking phone calls with clients daily. After two years, he was promoted to continue the same work, except with higher-risk clients. Two years later, he was once again promoted and now works as a manager for a team of Financial Advisors. 

One thing that Dylan loves to do is online shopping, specifically Amazon. He exclusively shops there. This is because much of his day is taken up by work, so online shopping is much more convenient for him. Additionally, moving around between Boston and Malvern sometimes causes him to put in the wrong address (the opposite one of where he is/will at a given time). Because of these two factors, he would find Knock-Knock useful for tracking his packages. When in Malvern, if a package is from Amazon, chances are it’s his. This way, he can be aware of/make his roommate aware that something he ordered arrived. Likewise, if it’s a package from anywhere else, it’s most likely his roommate’s, or a special package that he wasn’t expecting. Additionally, if the package was delivered in Boston, he would know that as well. This way, he can let his family know right away. 

### Talia
Lisa, age 38, runs a small boutique in the suburbs of Philadelphia where she sells handmade jewelry. She grew up in the area, and attended Tyler School of Art to study fine art. After graduation, she struggled to find a job, and pivoted to making jewelry and selling it online, where she found enough success to open a brick and mortar boutique after 5 years. She is married to a schoolteacher, and has 2 school age children, one who is 6 and one who is 8, meaning the house is left empty during the day. Although she runs her own business, Lisa tends to be a bit disorganized, and often mixes up personal and business accounts for various services. 

In the transition from online to brick and mortar, Lisa neglected to switch the address for shipping for a few of her accounts with the companies that provide her supplies. Her home is just a 5-minute drive from the boutique, so she often goes back and forth to pick up packages. Some of her supplies are sent through Amazon, but her essential materials come from specialty companies, and are delivered by FedEx and UPS. Also, almost all of her and her family’s personal packages are delivered through Amazon. Lisa would find Knock-Knock useful as a place where notifications about packages being delivered are aggregated, rather than being spread across different accounts, and she can decide, based on who delivered the package, whether she should leave the boutique to pick up the package, or should just leave it on her front porch for the day.

### Xufeng
Miss Jennifer, age 45, is the front desk office manager of a student residence hall on campus. Jennifer is dedicated to serve the community and help the students on campus. She loves to provide opportunities for the students on campus and hire them to work in the front desk office. As a very experienced front desk manager, Jennifer has been providing excellent front customer service for the residential hall for more than 20 years. Miss Jennifer went to Temple and have a degree in social science. She is a very organized person since day one and she likes to keep every i dotted, and every t crossed in the office. For a long, everything is done by hand, paper, and pen, but the office changed a lot in 20 years. Miss Jennifer adapted to using computers and software to run the office for better efficiency. However, some small places are still using the old school way in the office.

The residential hall houses more than 1000 thousand students, so there are a lot of people going in and out during the day, visitors, residents, staff on so on. One of the main functions of the front desk office is to receive packages for students and notify students to pick up at the office. Hundreds of packages delivered by different shipping companies are handled by the office every day. When a carrier stops by for delivery of twenty to thirty packages, the carrier asks for a sign as a record for the shipping company, and that’s all. The office does not have any means to keep track of who has been here to make delivery. Only Miss Jennifer remembers who has been here to deliver packages because she works full time.  But the students work at the office are all part-time, so if a FedEx stop by in the morning, the student at the afternoon shift does not know. Miss Jennifer finds this way very unproductive, and she is looking for an advanced, intelligent measure to keep track of the delivery record. 

### Brendan
Father Christian Condron is a 55-year-old catholic priest who leads a small parish in Collegeville, PA. He lived in this area his whole life and graduated from Archbishop John Carroll High School. After high school, he attended Temple University where he earned a bachelor’s degree in philosophy. He then decided to join a seminary and was ordained a priest 5 years later at the age of 32. He became the pastor of his parish 5 years ago after the former pastor passed away. On the weekends he offers mass and during the weekdays he does volunteer work and works as a substitute teacher at schools in the Archdiocese when needed.  

Recently, Father Condron started getting the communion wine delivered to his church’s address. It is usually delivered during the week when he is not around to pick it up and it ends up sitting outside until he returns. He realized that this will be a problem in the winter because the freezing temperatures could cause the bottle to burst. There is a camera installed but with other deliveries and people dropping off donations it is hard to tell when it arrives without checking his phone all day. He is interested in Knock-Knock since it will let him know when the wine arrives so he can stop by the church and put it inside. 

## Feature List
[Trello Board Link](https://trello.com/c/p2KyVKwq/7-feature-list)

