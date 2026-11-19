import numpy as np

class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = np.float64(data)
        self._grad = np.float64(0.)
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label
    
    def set_grad(self, value):
        self._grad = np.float64(value)

    def get_grad(self):
        return self._grad

    def __repr__(self):
        return f"Value(data={self.data}, label={self.label}, op='{self._op}')"
    
    def __add__(self, other):
        other = other if isinstance(other,Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')
        def _backward():
            self._grad += 1. * out._grad
            other._grad += 1. * out._grad
        out._backward = _backward
        return out

    def __radd__(self,other):
        return self + other

    def __mul__(self, other):
        other = other if isinstance(other,Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')
        def _backward():
            self._grad += other.data * out._grad
            other._grad += self.data * out._grad
        out._backward = _backward
        return out
    
    def __rmul__(self,other):
        return self * other

    def __truediv__(self, other):
        return self * other**-1

    def __pow__(self,other):
        assert isinstance(other,(int, float))
        out = Value(self.data**other, (self, ), f"**{other}")
        def _backward():
            self._grad += (other * self.data ** (other-1)) * out._grad
        out._backward = _backward
        return out
    
    def __neg__(self):
        return self * -1
    
    def __sub__(self, other):
        return self + (-other)
    
    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward():
            self._grad += (out.data > 0) * out._grad
        out._backward = _backward

        return out

    def tanh(self):
        n = self.data
        t = (np.exp(2*n) - 1) / (np.exp(2*n) + 1)
        out = Value(t, (self, ), 'tanh')

        def _backward():
            self._grad += (1 - t**2) * out._grad
            # out.grad = (1 - t**2) * self.grad
        out._backward = _backward

        return out
    
    def exp(self):
        x = self.data
        out = Value(np.exp(x), (self,), 'exp')

        def _backward():
            self._grad += out.data * out._grad 
        out._backward = _backward
        return out

    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        self._grad = np.float64(1.)

        for node in reversed(topo):
            node._backward()