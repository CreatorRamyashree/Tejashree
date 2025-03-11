student_data= {"id1" :
          {"name": ["Teja"], "class": [7], "subject_intigration": ["english, math, science"]
        }  ,

"id2" :
          {"name": ["Ramya"], "class": [8], "subject_intigration": ["english, math, science"]
        }  ,     
"id3" :
          {"name": ["Teja"], "class": [7], "subject_intigration": ["english, math, science"]
        }  ,
"id4" :
          {"name": ["Honey"], "class": [7], "subject_intigration": ["english, math, science"]
        }  ,
 }

result= {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
    
print(result)