select
    product,
    count(order_id)             as total_orders,
    sum(quantity)               as units_sold,
    sum(total_amount)           as revenue,
    avg(total_amount)           as avg_order_value,
    min(order_date)             as first_sale_date,
    max(order_date)             as last_sale_date
from {{ ref('stg_sales') }}
where status = 'completed'
group by product
order by revenue desc
