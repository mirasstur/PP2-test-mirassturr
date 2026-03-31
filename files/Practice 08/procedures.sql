--3. upset
CREATE OR REPLACE PROCEDURE upset_contacts(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE contact_name = p_name) THEN
        UPDATE contacts SET phone_number = p_phone WHERE contact_name = p_name;
    ELSE
        INSERT INTO contacts (contact_name, phone_number) VALUES (p_name, p_phone);
    END IF;
END;
$$;

--4. insert many
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_upper(p_names, 1) LOOP
        IF length(p_phones[i]) >= 10 THEN
            INSERT INTO contacts (contact_name, phone_number)
            VALUES (p_names[i], p_phones[i])
            ON CONFLICT (phone_number) DO UPDATE SET contact_name = EXCLUDED.contact_name;
        ELSE
            RAISE NOTICE 'Phone incor: %', p_phones[i];
        END IF;
    END LOOP;
END;
$$;

--5. delete data
CREATE OR REPLACE PROCEDURE delete_contact(p_search VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE contact_name = p_search or phone_number = p_search;
END;
$$;
