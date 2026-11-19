from graphviz import Digraph

def run(network, xinputs, target ,lr : float = -0.01, steps : int = 100):
    # llr = -0.05
    # steps = 20
    for k in range(steps):
        # forward pass
        ypred = [network(x) for x in xinputs]
        loss = sum([(yout - ygt)**2 for ygt, yout in zip(target, ypred)])

        # backward pass
        for p in network.parameters(): # Zero Grad
            p.set_grad = 0
        loss.backward()

        # update
        for p in network.parameters():
            p.data += lr * p.get_grad()
        
        print(f"{k:<5}{loss.data:<.20f}")
    return network

def get_pred(network, xinput):
    ypred = [network(x) for x in xinput]
    return ypred

def get_loss(ypred, target):
    loss= sum([(yout - ygt)**2 for ygt, yout in zip(target, ypred)])
    return loss


def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child,v))
                build(child)
    build(root)
    return nodes, edges

def draw_dot(root):
    dot = Digraph(
        format="svg",
        graph_attr={'rankdir':'LR'}
    )
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # print(uid)
        dot.node(
            name=uid,
            label=f"{n.label} | data: {n.data:.4f} | grad: {n.get_grad():.4f}",
            shape='record',
        )
        if n._op:
            dot.node(
                name=uid + n._op,
                label=n._op
            )
            dot.edge(uid + n._op, uid)
    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)


    return dot