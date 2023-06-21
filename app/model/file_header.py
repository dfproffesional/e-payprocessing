from config.database import Database
from sqlalchemy.orm import Mapped, Query, mapped_column
from sqlalchemy import Integer, String

class FileHeader(Database):
	__tablename__ = "file_header"
	
	id : Mapped[int] = mapped_column(Integer, primary_key= True)
	name : Mapped[str] = mapped_column(String)
	type : Mapped[str] = mapped_column(String)
	usage : Mapped[str] = mapped_column(String)
	comments : Mapped[str] = mapped_column(String)
	position : Mapped[str] = mapped_column(String)
	condition : Mapped[str] = mapped_column(String)
	description : Mapped[str] = mapped_column(String)

	def __init__(self):
		self.query : Query = self.session().query(__class__)
		super().__init__()

	def test(self):
		return self.query.all()
		