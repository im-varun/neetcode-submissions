class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        period, plus = ".", "+"
        at = "@"
        
        hashset = set()
        for email in emails:
            tokens = email.split(at)
            
            local_name = tokens[0]
            if period in local_name:
                local_name = "".join(local_name.split("."))
            if plus in local_name:
                local_name = local_name[0:local_name.index(plus)]

            domain_name = tokens[1]

            new_email = at.join([local_name, domain_name])
            if new_email not in hashset:
                hashset.add(new_email)

        count = len(hashset)

        return count