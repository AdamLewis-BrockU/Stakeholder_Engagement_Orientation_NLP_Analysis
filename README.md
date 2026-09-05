# Stakeholder_Engagement_Orientation_NLP_Analysis
Created by Adam Lewis. Includes jupyter notebooks (.ipynb files) written in python and markdown.


---


# **NOTES:**
1) The software I used to create these notebooks is Visual Studio Code.
2) If you want to download a jupyter notebook, please also download the MyPackages.py file. This stores all the packages used for each analysis.
3) If you want to download the Job_Postings_Stakeholder_Engagement.ipynb, you must also download the dataset to your computer. Please follow the link https://www.kaggle.com/datasets/promptcloud/indeed-job-posting-dataset to the dataset file and download it from Kaggle. Then, replace the file computer destination in pd.read_csv("C:\BROCK U COURSE DOCS\DataSets\marketing_sample_for_trulia_com-real_estate__20190901_20191031__30k_data.csv") with your own dataset file destination stored on your own computer. For example, if you send the dataset to your desktop, then it would be pd.read_csv("C:\Users\AdamD\Desktop\marketing_sample_for_trulia_com-real_estate__20190901_20191031__30k_data.csv).


---


# **10K_Filing_Stakeholder_EngagementOrientation.ipynb**

### **Data Analysis Steps:**
- Download 10-K filings from the SEC EDGAR database.
- Extract relevant sections (e.g., Item 1: Business, Item 7: MD&A) using regex or document parsing tools (e.g., BeautifulSoup, PyPDF2).
- Preprocess text to remove boilerplate language and normalize terms.
- Apply LDA to identify stakeholder engagement topics (e.g., employee welfare, customer satisfaction).
- Use BERT-based sentiment analysis to classify the tone of stakeholder mentions (e.g., positive vs. neutral).
- Quantify engagement frequency and correlate with financial metrics like return on equity or ESG scores.

### **Analysis Challenges:**
- Boilerplate language may obscure specific stakeholder engagement signals.
- Stakeholder terms vary by industry, requiring custom dictionaries.
- Lengthy documents demand efficient processing (e.g., chunking).

### **Analysis Example:**
- A 10-K might state: “We prioritize employee engagement through diversity programs and training.” NLP can extract “employee engagement” and “diversity programs,” classify the sentiment as positive, and quantify the firm’s orientation toward employees.

### **Data Destription:**
- UNITED STATES - SECURITIES AND EXCHANGE COMMISSION - Washington, D.C. 20549 - FORM 10-K
- For the fiscal year ended December 31, 2025 - Tesla, Inc.
- https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm#i39f9a11fdbe840828cbaefa2e098ffa8_151


---


# **Comment_Letters_Stakeholder_Engagement.ipynb**

### **Analysis Steps:**
- Collect comment letters from EDGAR or SEC correspondence databases.
- Preprocess letters to focus on stakeholder-related comments.
- Apply LDA to extract engagement themes (e.g., customer disclosure deficiencies).
- Use sentiment analysis to evaluate company response tone.
- Track issue resolution using sequence modeling or text similarity.

### **Challenges:**
- Technical regulatory language requires specialized NLP models.
- Limited public access to comment letters restricts analysis.
- Contextual understanding of stakeholder regulations is complex.

### **Example:**
- An SEC comment might state: “Provide additional disclosure on stakeholder engagement practices.” NLP can extract “stakeholder engagement” as a focus area and analyze the company’s response tone for compliance signals.

### **Information on Data Used:**
- For This analysis, two comment letters will be used: 
- NVIDIA's June 29, 2023 comment letter https://www.sec.gov/Archives/edgar/data/1045810/000104581023000160/filename1.htm, and
- NVIDIA's July 31, 2025 comment letter https://www.sec.gov/Archives/edgar/data/1045810/000104581025000192/filename1.htm.


---


# **Conference_Calls_Stakeholder_Engagement.ipynb**

### **Data Analysis Steps:**
- Obtain transcripts from platforms like Seeking Alpha or company investor relations pages.
- Preprocess transcripts to correct speech-to-text errors and segment by speaker.
- Apply KeyBERT to extract stakeholder keywords (e.g., “customer satisfaction,” “supplier partnerships”).
- Use sentiment analysis to evaluate the tone of stakeholder discussions.
- Train a classifier (e.g., XGBoost) to categorize engagement by stakeholder group (e.g., employees, customers).

### **Challenges:**
- Transcript errors from automated speech recognition can distort results.
- Brief mentions of stakeholders limit data depth.
- Non-verbal cues (e.g., tone of voice) are unavailable in text.

### **Example:**
- In a conference call, a CFO might say: “We’re investing heavily in customer experience to drive loyalty.” NLP can extract “customer experience” and “loyalty,” classify the tone as positive, and flag it as a customer-oriented signal.

### **About the Data used:**
- https://www.marketbeat.com/earnings/reports/2026-8-27-the-toronto-dominion-bank-stock/#transcript
- Toronto Dominion Bank (TD) Q3 2026 Earnings Report.
- Quarter: Q3 2026.
- Date: 8/27/2026.
- Time: Before Market Opens.
- Conference Call Date: Thursday, August 27, 2026.
- Conference Call Time: 9:30AM ET.


---


# **Job_Postings_Stakeholder_Engagement.ipynb**

### **Practical Steps:**
- Collect job postings from platforms like Indeed or company career pages.
- Preprocess postings to extract stakeholder-related roles and terms.
- Apply KeyBERT to identify engagement keywords (e.g., “community engagement,” “employee inclusion”).
- Use sentiment analysis to evaluate the tone of engagement-related descriptions.
- Cluster postings to identify industry trends in stakeholder orientation.

### **Challenges:**
- Brief job postings limit depth of analysis.
- Non-standardized terminology complicates processing.
- Internal postings are often inaccessible.

### **Example:**
- A job posting for a “Community Engagement Specialist” might emphasize “building stakeholder relationships.” NLP can extract “stakeholder relationships,” classify the tone as positive, and correlate it with ESG performance.

### **About the Data:**
- https://www.kaggle.com/datasets/PromptCloudHQ/jobs-on-naukricom
- The dataset was found on Kaggle.com, and was created by PromptCloud.


---


# **Proxy_Statements_Stakeholder_Engagement.ipynb**

### **Data Analysis Steps:**
- Collect proxy statements from EDGAR or company websites.
- Preprocess text to focus on governance and shareholder proposal sections.
- Apply LDA to identify stakeholder engagement themes (e.g., employee welfare, community outreach).
- Use sentiment analysis to evaluate the tone of stakeholder discussions.
- Track changes in engagement language across years using cosine similarity.

### **Challenges:**
- Stakeholder engagement is often a secondary focus, limiting data volume.
- Governance language is vague, requiring contextual NLP models.
- Limited historical data restricts longitudinal analysis.

### **Example:**
- A proxy statement might mention: “Shareholders propose increased stakeholder engagement through community programs.” NLP can extract “stakeholder engagement” and “community programs,” assessing their governance implications.

### **About the Data used:**
- https://www.sec.gov/Archives/edgar/data/1065088/000110465925042545/tm2424429-2_def14a.htm
- UNITED STATES - SECURITIES AND EXCHANGE COMMISSION - Washington, D.C. 20549​
- SCHEDULE 14A - Proxy Statement Pursuant to Section 14(a) of the Securities - Exchange Act of 1934 (Amendment No.  )
- Ebay Inc. 2025 Annual Proxy Statement

