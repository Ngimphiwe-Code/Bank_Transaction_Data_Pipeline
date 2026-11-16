
-- 1. Overall transaction statistics
SELECT
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount)::numeric, 2) AS average_amount,
    MIN(amount) AS smallest_transaction,
    MAX(amount) AS largest_transaction
FROM public.transactions;


-- 2. Transaction statistics by category
SELECT
    category,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount)::numeric, 2) AS average_amount,
    MIN(amount) AS smallest_amount,
    MAX(amount) AS largest_amount
FROM public.transactions
GROUP BY category
ORDER BY total_amount DESC;


-- 3. Transaction totals by location
SELECT
    location,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM public.transactions
GROUP BY location
ORDER BY total_amount DESC;


-- 4. High-value transactions
SELECT
    transaction_id,
    customer_id,
    amount,
    transaction_date,
    location
FROM public.transactions
WHERE amount > 5000
ORDER BY amount DESC;


-- 5. Rank transactions by amount
SELECT
    transaction_id,
    customer_id,
    amount,
    location,
    RANK() OVER (
        ORDER BY amount DESC
    ) AS transaction_rank
FROM public.transactions
ORDER BY amount DESC;

