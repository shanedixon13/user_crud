from app.database import get_db



def output_formatter(results: tuple):
    out=[]
    for result in results:
        result_dict={}
        result_dict["id"]=result[0]
        result_dict["first_name"]=result[1]
        result_dict["last_name"]=result[2]
        result_dict["hobbies"]=result[3]
        result_dict["active"]=result[4]
        out.append(result_dict)
    return out


def insert(first_name, last_name, hobbies=None, active=1):
    value_tuple=(first_name, last_name, hobbies, active)
    query="""
        INSERT INTO user (
            first_name,
            last_name,
            hobbies,
            active
        ) VALUES (
            ?, ?, ?, ?
        )
    """
    curser=get_db()
    last_row_id=curser.execute(query, value_tuple).lastrowid
    curser.commit()
    curser.close()
    return last_row_id