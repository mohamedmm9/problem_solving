class Solution:
    def middleNode(self, head):
        nodeList = []
        while head!=None:
            nodeList.append(head)
            head = head.next
        return nodeList[len(nodeList)//2]
