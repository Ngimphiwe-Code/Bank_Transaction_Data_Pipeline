
-- 1. Overall transaction statistics
SELECT
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount)::numeric, 2) AS average_amount,
    MIN(amount) AS smallest_transaction,
    MAX(amount) AS largest_transaction
FROM transactions;

-- 2. Transaction statistics by category
SELECT
    category,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount)::numeric, 2) AS average_amount,
    MIN(amount) AS smallest_amount,
    MAX(amount) AS largest_amount
FROM transactions
GROUP BY category
ORDER BY total_amount DESC;
