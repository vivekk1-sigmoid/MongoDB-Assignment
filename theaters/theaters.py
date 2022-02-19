# 1.	Top 10 cities with the maximum number of theatres

db.getCollection('theaters').aggregate([
        {"$group": {"_id": {"city": "$location.address.city"}, "totalTheaters": {"$sum": 1}}},
        {"$sort": {"totalTheaters": -1}},
        {"$project": {"city": "$_id.city", "totalTheaters": 1}},
        {"$limit": 10}
    ])




# 2.	top 10 theatres nearby given coordinates
# some problem with the output
db.getCollection('theaters').find({
        "location.geo": 
            {
                    "$near": 
                    {
                        "$geometry": {"type": "Point", "coordinates": [-93.24565, 44.85466]},  
                    }
                }
    }).limit(10)


