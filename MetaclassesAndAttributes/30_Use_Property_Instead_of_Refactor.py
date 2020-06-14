# Item 30: Consider Property Intead Of Refactoring
"""
1. Transfer a simple numerical attribute into a on-the-fly calculation
2. Using @property gives existing attributes a new functionality
3. Use property for incremental improvements
4. Don't abuse it
"""

# Setup
from datetime import datetime, timedelta


# Option 1:
"""
When the deduction fails, we don't know because of we want to deduct too much or it does not have enough quota
"""
class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.quota = 0

	def __repr__(self):
		return f'Bucket Quota: {self.quota}'

def fill(bucket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		bucket.quota = 0
		bucket.reset_time = now

	bucket.quota = bucket.quota + amount

def deduct(bucket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		return False

	if bucket.quota - amount < 0:
		return False

	bucket.quota = bucket.quota - amount
	return True


# Option 2:
class NewBucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.max_quota = 0
		self.quota_consumed = 0

	def __repr__(self):
		return f'NewBucket Max Quota: {self.quota}, Quota Consumed: {self.quota_consumed}'

	@property
	def quota(self):
		return self.max_quota - self.quota_consumed

	@quota.setter
	def quota(self, amount):
		delta = self.max_quota - amount
		if amount == 0:
			# Reset
			self.quota_consumed = 0
			self.max_quota = 0

		elif delta < 0:
			# Quota being refilled for the new period
			assert self.quota_consumed == 0
			self.max_quota = amount

		else:
			assert self.max_quota >= self.quota_consumed
			self.quota_consumed = self.quota_consumed + delta

bucket1 = Bucket(60)
fill(bucket1, 100)
print(bucket1)

bucket2 = NewBucket(60)
fill(bucket2, 100)
print(bucket2)


def testcase(bucket):
	if deduct(bucket, 99):
		print(f'deduct 99')
	else:
		print(f'Not Enought Quota')

	if deduct(bucket, 3):
		print(f'deduct 3')
	else:
		print(f'Not Enought Quota')

	print(bucket)

testcase(bucket1)
testcase(bucket2)

	





