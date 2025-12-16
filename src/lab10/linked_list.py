from typing import Any, Optional, Iterator


class Node:
    """Узел односвязного списка."""
    
    def __init__(self, value: Any) -> None:
        """Инициализация узла.
        
        Args:
            value: Значение узла.
        """
        self.value: Any = value
        self.next: Optional['Node'] = None
    
    def __repr__(self) -> str:
        """Вернуть строковое представление узла.
        
        Returns:
            Строковое представление узла.
        """
        return f"Node({self.value})"


class SinglyLinkedList:
    """Односвязный список, состоящий из узлов Node."""
    
    def __init__(self, iterable: Optional[Any] = None) -> None:
        """Инициализация односвязного списка.
        
        Args:
            iterable: Итерируемый объект для инициализации списка.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
        
        if iterable is not None:
            for item in iterable:
                self.append(item)
    
    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка.
        
        Args:
            value: Значение для добавления.
        """
        new_node = Node(value)
        
        if self.head is None:  # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:  # Если список не пуст
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка.
        
        Args:
            value: Значение для добавления.
        """
        new_node = Node(value)
        
        if self.head is None:  # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:  # Если список не пуст
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """Вставить элемент по индексу idx.
        
        Args:
            idx: Индекс для вставки.
            value: Значение для вставки.
            
        Raises:
            IndexError: Если индекс вне диапазона [0, len(list)].
        """
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        
        if idx == 0:  # Вставка в начало
            self.prepend(value)
        elif idx == self._size:  # Вставка в конец
            self.append(value)
        else:  # Вставка в середину
            new_node = Node(value)
            current = self.head
            
            # Переходим к элементу перед позицией вставки
            for _ in range(idx - 1):
                current = current.next  # type: ignore
            
            new_node.next = current.next  # type: ignore
            current.next = new_node  # type: ignore
            self._size += 1
    
    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу idx.
        
        Args:
            idx: Индекс элемента для удаления.
            
        Raises:
            IndexError: Если индекс вне диапазона [0, len(list)-1].
        """
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size-1}]")
        
        if idx == 0:  # Удаление первого элемента
            self.head = self.head.next  # type: ignore
            if self.head is None:  # Если список стал пустым
                self.tail = None
        else:  # Удаление из середины или конца
            current = self.head
            
            # Переходим к элементу перед удаляемым
            for _ in range(idx - 1):
                current = current.next  # type: ignore
            
            # Если удаляем последний элемент
            if idx == self._size - 1:
                current.next = None  # type: ignore
                self.tail = current
            else:
                current.next = current.next.next  # type: ignore
        
        self._size -= 1
    
    def remove(self, value: Any) -> bool:
        """Удалить первое вхождение значения value.
        
        Args:
            value: Значение для удаления.
            
        Returns:
            True, если элемент был найден и удален, иначе False.
        """
        if self.head is None:
            return False
        
        # Если удаляем первый элемент
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # Поиск элемента для удаления
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                
                # Если удаляем последний элемент
                if current.next is None:
                    self.tail = current
                
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def __iter__(self) -> Iterator[Any]:
        """Вернуть итератор по значениям в списке.
        
        Returns:
            Итератор по значениям списка.
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """Вернуть количество элементов в списке.
        
        Returns:
            Количество элементов в списке.
        """
        return self._size
    
    def __repr__(self) -> str:
        """Вернуть строковое представление списка.
        
        Returns:
            Строковое представление списка.
        """
        values = list(self)
        return f"SinglyLinkedList({values})"