import graphene
from graphene import AbstractType, InputObjectType
from graphene_django.types import DjangoObjectType
from home.models import SinhVien
from datetime import date
class SinhVienType(DjangoObjectType):
    class Meta:
        model = SinhVien

class CreateSinhVien(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    msv = graphene.String()
    lop = graphene.String()
    ngaysinh = graphene.Date()
    class Arguments:
        name = graphene.String()
        msv = graphene.String()
        lop = graphene.String()
        ngaysinh = graphene.Date()
    def mutate(self, info, name, ngaysinh, msv = "", lop = ""):
        sinhVien = SinhVien(name = name, msv = msv, lop = lop, ngaysinh = ngaysinh)
        sinhVien.save()
        return CreateSinhVien(id = sinhVien.id, name = sinhVien.name, msv = sinhVien.msv, lop = sinhVien.lop, ngaysinh = sinhVien.ngaysinh)

class UpdateSinhVien(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    msv = graphene.String()
    lop = graphene.String()
    ngaysinh = graphene.Date()
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        msv = graphene.String()
        lop = graphene.String()
        ngaysinh = graphene.Date()
    def mutate(self, info, id, name = None, ngaysinh = None, msv = None, lop = None):
        try:
            id = int(id)
        except ValueError:
            raise Exception("ID không hợp lệ: {}".format(id))
                
        sinhVien = SinhVien.objects.get(pk = id)
        if sinhVien is None:
            raise Exception("ID không hợp lệ: {}".format(id))
        if name is not None:
            sinhVien.name = name
        if ngaysinh is not None:
            sinhVien.ngaysinh = ngaysinh
        if msv is not None:
            sinhVien.msv = msv
        if lop is not None:
            sinhVien.lop = lop
        sinhVien.save()
        return CreateSinhVien(id = sinhVien.id, name = sinhVien.name, msv = sinhVien.msv, lop = sinhVien.lop, ngaysinh = sinhVien.ngaysinh)

class DeleteSinhVien(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    msv = graphene.String()
    lop = graphene.String()
    ngaysinh = graphene.Date()
    class Arguments:
        id = graphene.Int()
    def mutate(self, info, id):
        try:
            id = int(id)
        except ValueError:
            raise Exception("ID không hợp lệ: {}".format(id))                
        sinhVien = SinhVien.objects.get(pk = id)
        sinhVien.delete()
        return CreateSinhVien(id = sinhVien.id, name = sinhVien.name, msv = sinhVien.msv, lop = sinhVien.lop, ngaysinh = sinhVien.ngaysinh)        

class Query(object):
    all_sinhvien = graphene.List(SinhVienType)
    sinhvien = graphene.Field(SinhVienType, id=graphene.Int(), name=graphene.String(), msv=graphene.String())
    def resolve_all_sinhvien(self, info, **kwargs):
        return SinhVien.objects.all()
    def resolve_sinhvien(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        msv = kwargs.get('msv')
        if id is not None:
            return SinhVien.objects.get(pk=id)
        if name is not None:
            return SinhVien.objects.get(name=name)
        if msv is not None:
            return SinhVien.objects.get(msv=msv)
        return None

class SinhVienMutations(AbstractType):
    update_SinhVien = UpdateSinhVien.Field()
    create_SinhVien = CreateSinhVien.Field()
    delete_SinhVien = DeleteSinhVien.Field()
    