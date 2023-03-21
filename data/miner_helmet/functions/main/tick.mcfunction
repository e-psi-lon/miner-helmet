execute as @a if predicate miner_helmet:has_miner_helmet run tag @s add miner_helmet.has_helmet
execute as @a[tag=miner_helmet.has_helmet] unless predicate miner_helmet:has_miner_helmet run tag @s remove miner_helmet.has_helmet
execute as @e[type=marker,tag=is_for_light] at @s run function miner_helmet:main/delete
execute as @a[tag=miner_helmet.has_helmet] at @s run function miner_helmet:main/place_light