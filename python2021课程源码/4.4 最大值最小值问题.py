
#最大值最小值问题

scores=[67,78,56,89,76,79,98,45,65,76]

#最高分数
maxScore=scores[0]
for score in scores:
	if score>maxScore:
		maxScore=score #将更大值更新为最大值
print(maxScore)


#最低分数
minScore=scores[0]
for score in scores:
	if score<minScore:
		minScore=score #将更小值更新为最小值
print(minScore)

