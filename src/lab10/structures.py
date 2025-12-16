from collections import deque
from typing import Any, Optional


class Stack:
    """Структура данных 'стек' (LIFO) на базе list."""
    
    def __init__(self) -> None:
        """Инициализация пустого стека."""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека.
        
        Args:
            item: Элемент для добавления.
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """Снять верхний элемент стека и вернуть его.
        
        Returns:
            Элемент с вершины стека.
            
        Raises:
            IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Нельзя извлечь элемент из пустого стека")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        """Вернуть верхний элемент без удаления.
        
        Returns:
            Элемент с вершины стека или None, если стек пуст.
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """Проверить, пуст ли стек.
        
        Returns:
            True, если стек пуст, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Вернуть количество элементов в стеке.
        
        Returns:
            Количество элементов в стеке.
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        """Вернуть строковое представление стека.
        
        Returns:
            Строковое представление стека.
        """
        return f"Stack({self._data})"


class Queue:
    """Структура данных 'очередь' (FIFO) на базе collections.deque."""
    
    def __init__(self) -> None:
        """Инициализация пустой очереди."""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди.
        
        Args:
            item: Элемент для добавления.
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """Взять элемент из начала очереди и вернуть его.
        
        Returns:
            Элемент из начала очереди.
            
        Raises:
            IndexError: Если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("Нельзя извлечь элемент из пустой очереди")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        """Вернуть первый элемент без удаления.
        
        Returns:
            Первый элемент очереди или None, если очередь пуста.
        """
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь.
        
        Returns:
            True, если очередь пуста, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Вернуть количество элементов в очереди.
        
        Returns:
            Количество элементов в очереди.
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        """Вернуть строковое представление очереди.
        
        Returns:
            Строковое представление очереди.
        """
        return f"Queue({list(self._data)})"