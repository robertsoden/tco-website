# LinkedIn Post Images - Download Instructions

Download these images manually from LinkedIn and save them to the specified locations.

**Total images to download: 8**

## Quick Reference

You can download images using these methods:

### Method 1: Manual Download
1. Open each image URL in your browser
2. Right-click and "Save image as..."
3. Save to the location specified below

### Method 2: Command Line (curl)
```bash
# Create directory if needed
mkdir -p assets/images/news

# Download all images (copy/paste these commands)
curl -L 'https://media.licdn.com/dms/image/sync/v2/D4E27AQE8_F8em9ZN7g/articleshare-shrink_160/B4EZqR6Th0IIAk-/0/1763384572730?e=1764136800\&v=beta\&t=d6gYPALkwUdO_nSiZK0LpGSIRjuOT12xT70hJxY8DM8' -o 'assets/images/news/2025-11-18-two-weeks-ago-the-climate-aligned-finance-act-cafa-was-reint.jpg'
curl -L 'https://media.licdn.com/dms/image/v2/D5622AQEl8RGQCqHXNw/feedshare-shrink_800/B56Zm6rbGBIsAk-/0/1759773572747?e=1765411200\&v=beta\&t=EA_CMUpUyuGQvm053qEIbfpgyIYefyWlMEQfB-VuxW4' -o 'assets/images/news/2025-11-19-workshop-alert.jpg'
curl -L 'https://media.licdn.com/dms/image/v2/D5622AQFUhXKKzR1S0w/feedshare-shrink_800/B56Zk_yUIxHMAg-/0/1757711780564?e=1765411200\&v=beta\&t=TML45UcBkC5g3Lhs9A_F57P3y_lfERswrrVNwi5Vs6o' -o 'assets/images/news/2025-11-19-tco-voices-hear-from-dylan-van-bramer-a-new-addition-to-the.jpg'
curl -L 'https://media.licdn.com/dms/image/v2/D5622AQE-a80entSuNQ/feedshare-shrink_800/B56ZjTbu2jHQAk-/0/1755893920702?e=1765411200\&v=beta\&t=G8gY1ArmQ1JFvymumcLAal-xsEjXpkgzay6FSWbQrqg' -o 'assets/images/news/2025-09-20-project-spotlight-reimagining-our-relationship-with-water-th.jpg'
curl -L 'https://media.licdn.com/dms/image/v2/D5622AQHzbbbR-4UssQ/feedshare-shrink_800/B56ZigeDVdG4Ag-/0/1755038890735?e=1765411200\&v=beta\&t=wI56kPc1OBr0jy9bLc72P6wVgFJDN74J6bzTH42rPq0' -o 'assets/images/news/2025-11-19-glimpses-from-compass-2025-hosted-by-university-of-toronto-a.jpg'
curl -L 'https://media.licdn.com/dms/image/v2/D5622AQEvXwtMCGepdw/feedshare-shrink_800/B56ZiGnUqGG4Ak-/0/1754605112530?e=1765411200\&v=beta\&t=xnVDXeVxl3awMvezEuSqPt2auBqVU6BtExQsxbRhHlM' -o 'assets/images/news/2025-08-21-from-july-22-25-university-of-toronto-hosted-the-2025-iterat.jpg'
curl -L 'https://media.licdn.com/dms/image/sync/v2/D5627AQGx-VlvBJ97zw/articleshare-shrink_480/B56Zf01rnmHYAo-/0/1752159402910?e=1764136800\&v=beta\&t=wmm8vTheN2jx1wwZxsNy4SuJqtSVNzyj_-BW0AGuw8Y' -o 'assets/images/news/2025-11-19-event-recap-the-looming-lng-glut-market-assessment-risks-thi.jpg'
curl -L 'https://media.licdn.com/dms/image/v2/D5622AQE3SRhxQE9zFg/feedshare-shrink_800/B56ZfxRYWVHQAs-/0/1752099562946?e=1765411200\&v=beta\&t=kB7nDb66_MReqexjUa6Sw7YK_7OR8PMes9OqtI9SZzQ' -o 'assets/images/news/2025-07-22-last-month-we-officially-wrapped-up-the-toronto-climate-summ.jpg'
```

### Method 3: Command Line (wget)
```bash
# Create directory if needed
mkdir -p assets/images/news

# Download all images
wget 'https://media.licdn.com/dms/image/sync/v2/D4E27AQE8_F8em9ZN7g/articleshare-shrink_160/B4EZqR6Th0IIAk-/0/1763384572730?e=1764136800&v=beta&t=d6gYPALkwUdO_nSiZK0LpGSIRjuOT12xT70hJxY8DM8' -O 'assets/images/news/2025-11-18-two-weeks-ago-the-climate-aligned-finance-act-cafa-was-reint.jpg'
wget 'https://media.licdn.com/dms/image/v2/D5622AQEl8RGQCqHXNw/feedshare-shrink_800/B56Zm6rbGBIsAk-/0/1759773572747?e=1765411200&v=beta&t=EA_CMUpUyuGQvm053qEIbfpgyIYefyWlMEQfB-VuxW4' -O 'assets/images/news/2025-11-19-workshop-alert.jpg'
wget 'https://media.licdn.com/dms/image/v2/D5622AQFUhXKKzR1S0w/feedshare-shrink_800/B56Zk_yUIxHMAg-/0/1757711780564?e=1765411200&v=beta&t=TML45UcBkC5g3Lhs9A_F57P3y_lfERswrrVNwi5Vs6o' -O 'assets/images/news/2025-11-19-tco-voices-hear-from-dylan-van-bramer-a-new-addition-to-the.jpg'
wget 'https://media.licdn.com/dms/image/v2/D5622AQE-a80entSuNQ/feedshare-shrink_800/B56ZjTbu2jHQAk-/0/1755893920702?e=1765411200&v=beta&t=G8gY1ArmQ1JFvymumcLAal-xsEjXpkgzay6FSWbQrqg' -O 'assets/images/news/2025-09-20-project-spotlight-reimagining-our-relationship-with-water-th.jpg'
wget 'https://media.licdn.com/dms/image/v2/D5622AQHzbbbR-4UssQ/feedshare-shrink_800/B56ZigeDVdG4Ag-/0/1755038890735?e=1765411200&v=beta&t=wI56kPc1OBr0jy9bLc72P6wVgFJDN74J6bzTH42rPq0' -O 'assets/images/news/2025-11-19-glimpses-from-compass-2025-hosted-by-university-of-toronto-a.jpg'
wget 'https://media.licdn.com/dms/image/v2/D5622AQEvXwtMCGepdw/feedshare-shrink_800/B56ZiGnUqGG4Ak-/0/1754605112530?e=1765411200&v=beta&t=xnVDXeVxl3awMvezEuSqPt2auBqVU6BtExQsxbRhHlM' -O 'assets/images/news/2025-08-21-from-july-22-25-university-of-toronto-hosted-the-2025-iterat.jpg'
wget 'https://media.licdn.com/dms/image/sync/v2/D5627AQGx-VlvBJ97zw/articleshare-shrink_480/B56Zf01rnmHYAo-/0/1752159402910?e=1764136800&v=beta&t=wmm8vTheN2jx1wwZxsNy4SuJqtSVNzyj_-BW0AGuw8Y' -O 'assets/images/news/2025-11-19-event-recap-the-looming-lng-glut-market-assessment-risks-thi.jpg'
wget 'https://media.licdn.com/dms/image/v2/D5622AQE3SRhxQE9zFg/feedshare-shrink_800/B56ZfxRYWVHQAs-/0/1752099562946?e=1765411200&v=beta&t=kB7nDb66_MReqexjUa6Sw7YK_7OR8PMes9OqtI9SZzQ' -O 'assets/images/news/2025-07-22-last-month-we-officially-wrapped-up-the-toronto-climate-summ.jpg'
```

## Detailed Image List

### 1. Two weeks ago the Climate Aligned Finance Act CAFA was reintroduced into the Sen...

**Post Date:** 2025-11-18

**Image URL:**
```
https://media.licdn.com/dms/image/sync/v2/D4E27AQE8_F8em9ZN7g/articleshare-shrink_160/B4EZqR6Th0IIAk-/0/1763384572730?e=1764136800&v=beta&t=d6gYPALkwUdO_nSiZK0LpGSIRjuOT12xT70hJxY8DM8
```

**Save to:**
```
assets/images/news/2025-11-18-two-weeks-ago-the-climate-aligned-finance-act-cafa-was-reint.jpg
```

---

### 2. Workshop alert

**Post Date:** 2025-11-19

**Image URL:**
```
https://media.licdn.com/dms/image/v2/D5622AQEl8RGQCqHXNw/feedshare-shrink_800/B56Zm6rbGBIsAk-/0/1759773572747?e=1765411200&v=beta&t=EA_CMUpUyuGQvm053qEIbfpgyIYefyWlMEQfB-VuxW4
```

**Save to:**
```
assets/images/news/2025-11-19-workshop-alert.jpg
```

---

### 3. TCO Voices Hear from Dylan Van Bramer a new addition to the TCO

**Post Date:** 2025-11-19

**Image URL:**
```
https://media.licdn.com/dms/image/v2/D5622AQFUhXKKzR1S0w/feedshare-shrink_800/B56Zk_yUIxHMAg-/0/1757711780564?e=1765411200&v=beta&t=TML45UcBkC5g3Lhs9A_F57P3y_lfERswrrVNwi5Vs6o
```

**Save to:**
```
assets/images/news/2025-11-19-tco-voices-hear-from-dylan-van-bramer-a-new-addition-to-the.jpg
```

---

### 4. Project Spotlight Reimagining our relationship with water through the Toronto Wa...

**Post Date:** 2025-09-20

**Image URL:**
```
https://media.licdn.com/dms/image/v2/D5622AQE-a80entSuNQ/feedshare-shrink_800/B56ZjTbu2jHQAk-/0/1755893920702?e=1765411200&v=beta&t=G8gY1ArmQ1JFvymumcLAal-xsEjXpkgzay6FSWbQrqg
```

**Save to:**
```
assets/images/news/2025-09-20-project-spotlight-reimagining-our-relationship-with-water-th.jpg
```

---

### 5. Glimpses from COMPASS 2025 hosted by University of Toronto as captured by and fe...

**Post Date:** 2025-11-19

**Image URL:**
```
https://media.licdn.com/dms/image/v2/D5622AQHzbbbR-4UssQ/feedshare-shrink_800/B56ZigeDVdG4Ag-/0/1755038890735?e=1765411200&v=beta&t=wI56kPc1OBr0jy9bLc72P6wVgFJDN74J6bzTH42rPq0
```

**Save to:**
```
assets/images/news/2025-11-19-glimpses-from-compass-2025-hosted-by-university-of-toronto-a.jpg
```

---

### 6. From July 22 - 25 University of Toronto hosted the 2025 iteration of the ACM Ass...

**Post Date:** 2025-08-21

**Image URL:**
```
https://media.licdn.com/dms/image/v2/D5622AQEvXwtMCGepdw/feedshare-shrink_800/B56ZiGnUqGG4Ak-/0/1754605112530?e=1765411200&v=beta&t=xnVDXeVxl3awMvezEuSqPt2auBqVU6BtExQsxbRhHlM
```

**Save to:**
```
assets/images/news/2025-08-21-from-july-22-25-university-of-toronto-hosted-the-2025-iterat.jpg
```

---

### 7. Event Recap The Looming LNG Glut  Market Assessment  Risks

This week the TCO co...

**Post Date:** 2025-11-19

**Image URL:**
```
https://media.licdn.com/dms/image/sync/v2/D5627AQGx-VlvBJ97zw/articleshare-shrink_480/B56Zf01rnmHYAo-/0/1752159402910?e=1764136800&v=beta&t=wmm8vTheN2jx1wwZxsNy4SuJqtSVNzyj_-BW0AGuw8Y
```

**Save to:**
```
assets/images/news/2025-11-19-event-recap-the-looming-lng-glut-market-assessment-risks-thi.jpg
```

---

### 8. Last month we officially wrapped up the Toronto Climate Summer School TCSS after...

**Post Date:** 2025-07-22

**Image URL:**
```
https://media.licdn.com/dms/image/v2/D5622AQE3SRhxQE9zFg/feedshare-shrink_800/B56ZfxRYWVHQAs-/0/1752099562946?e=1765411200&v=beta&t=kB7nDb66_MReqexjUa6Sw7YK_7OR8PMes9OqtI9SZzQ
```

**Save to:**
```
assets/images/news/2025-07-22-last-month-we-officially-wrapped-up-the-toronto-climate-summ.jpg
```

---

