select
    order_id,
    customer_id,
    lower(trim(product))        as product,
    quantity,
    unit_price,
    quantity * unit_price       as total_amount,
    order_date,
    lower(trim(status))         as status,
    load_timestamp
from {{ source('raw', 'sales_raw') }}
where order_id is not null
