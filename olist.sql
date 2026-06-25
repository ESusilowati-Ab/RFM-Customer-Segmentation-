CREATE TABLE rfm_analysis (
    customer_unique_id VARCHAR(50),
    recency INTEGER,
    frequency INTEGER,
    monetary NUMERIC(12,2),
    r_score INTEGER,
    f_score INTEGER,
    m_score INTEGER,
    rfm_score_group VARCHAR(10),
    segment VARCHAR(100)
);

SELECT *
FROM rfm_analysis
LIMIT 10;

# 1. Customer Count by Segment

SELECT
    segment,
    COUNT(*) AS customer_count
FROM rfm_analysis
GROUP BY segment
ORDER BY customer_count DESC;

#2. Percentage Distribution of Segments

SELECT
    segment,
    COUNT(*) AS customer_count,
    ROUND(
        COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM rfm_analysis
GROUP BY segment
ORDER BY customer_count DESC;

#3. Average RFM Metrics by Segment

SELECT
    segment,
    ROUND(AVG(recency), 1) AS avg_recency,
    ROUND(AVG(frequency), 1) AS avg_frequency,
    ROUND(AVG(monetary), 1) AS avg_monetary
FROM rfm_analysis
GROUP BY segment
ORDER BY avg_monetary DESC;

#4. Top 10 Highest-Spending Customers

SELECT
    customer_unique_id,
    monetary
FROM rfm_analysis
ORDER BY monetary DESC
LIMIT 10;

#5. Customers at Risk

SELECT *
FROM rfm_analysis
WHERE segment = 'At Risk';

#6. Champions Customers

SELECT *
FROM rfm_analysis
WHERE segment = 'Champions';


SELECT *
FROM rfm_analysis
LIMIT 10;


# Segment Distribution

SELECT
    segment,
    COUNT(*) AS customer_count
FROM rfm_analysis
GROUP BY segment
ORDER BY customer_count DESC;


