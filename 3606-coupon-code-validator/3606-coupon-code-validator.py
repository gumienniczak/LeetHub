class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        n = len(code)
        valid_codes = []
        ans = []
        for i in range(n):
            idx = code[i]
            business = businessLine[i]
            status = isActive[i]
            if (idx and (idx.replace("_", "").isalnum() or idx == '_')) and (business and business in ['electronics', 'grocery', 'pharmacy', 'restaurant']) and status:
                valid_codes.append((idx, business))
            
        valid_codes.sort(key = lambda x: (x[1], x[0]))
        return [code[0] for code in valid_codes]