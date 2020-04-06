from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, PickleType
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

"""
This is an order history class that holds an orderId, an orderDate, and an array of items that were ordered.
"""
class OrderHistory(Base):
    def __init__(self, orderId, orderDate, itemsOrdered):
        self.orderId = orderId
        self.itemsOrdered = itemsOrdered
        self.orderDate = orderDate
        
    __tablename__ = 'ORDER_HISTORY'
    
    id = Column(Integer, primary_key=True)
    orderId = Column('ORDER_ID', Integer)
    itemsOrdered = Column('ITEMS_ORDERED', PickleType)
    orderDate = Column('ORDER_DATE', DateTime)
    
    def __repr(self):
        return ('<OrderId={}, itemsOrdered={}, orderDate={}>'
                .format(self.orderId, self.itemsOrdered, self.orderDate))
        
    def __str__(self): 
        return ('Order History is OrderId: {}, ItemsOrdered: {}, OrderDate: {}'
                .format(self.orderId, self.itemsOrdered, self.orderDate))
    

def main():
    # Creating Connection
    engine = create_engine('sqlite:///:memory:', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # adding one record
    orderOne = OrderHistory('1234567891', datetime.utcnow(), ['item1','item2','item3'])
    print(orderOne)
    session.add(orderOne)
    session.commit()
    
    # retrieving the same record
    orderOneReturned = session.query(OrderHistory).filter_by(orderId='1234567891').first()
    print(orderOneReturned)
    
    session.close()

main()