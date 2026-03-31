CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_pattern TEXT)
RETURNS TABLE(contact_id INT, contact_name VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.contact_id, c.contact_name, c.phone_number 
    FROM contacts c
    WHERE c.contact_name ILIKE '%' || p_pattern || '%' 
       OR c.phone_number ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

--2. pagination

CREATE OR REPLACE FUNCTION get_contacts_paged(p_limit INT, p_offset INT)
RETURNS TABLE(contact_id INT, contact_name VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.contact_id, c.contact_name, c.phone_number 
    FROM contacts c
    ORDER BY c.contact_name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;