class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        mentions = [0] * numberOfUsers
        users_online = [1] * numberOfUsers
        timestamps = [0] * numberOfUsers

        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == 'OFFLINE' else 1))

        for event in events:
            tp = event[0] 
            ts = int(event[1])
            who = event[2] 
            if tp == 'OFFLINE':
                timestamps[int(who)] = ts
                users_online[int(who)] = 0
            
            for idx in range(numberOfUsers):
                if timestamps[idx] + 60 <= ts:
                    users_online[idx] = 1
            
            if tp == 'MESSAGE':
                if who == 'ALL':
                    for idx in range(numberOfUsers):
                        mentions[idx] += 1
                elif who == 'HERE':
                    for idx in range(numberOfUsers):
                        if users_online[idx]:
                            mentions[idx] += 1
                else:
                    for user in who.split():
                        mentions[int(user[2:])] += 1

        return mentions
            
