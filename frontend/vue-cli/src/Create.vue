<script>
import gql from 'graphql-tag';
const createSinhVien = gql`
  mutation ($_name:String!, $_msv:String!,$_lop:String!,$_ngaysinh:Date!) {
    createSinhvien(name: $_name, msv: $_msv, lop: $_lop, ngaysinh: $_ngaysinh) {
      id
      name
      msv
      lop
      ngaysinh
    }
  }
`;
export default {
  props: {
    id: {type: Number},
    name: {type: String},
    msv: {type: String},
    lop: {type: String},
    ngaysinh: {type: String},
  },
  methods: {
    create() {
      this.$apollo.mutate({
        mutation: createSinhVien,
        variables: {
          _name: this.name,
          _msv: this.msv,
          _lop: this.lop,
          _ngaysinh: this.ngaysinh,
        },
      }).then(data => {
        console.log('Done Create.');
      });
    },
  },
};
</script>

<template>
    <div>
        <input v-model="name" placeholder="Họ tên">
        <input v-model="msv" placeholder="Mã sinh viên">
        <input v-model="lop" placeholder="Lớp">
        <input v-model="ngaysinh" placeholder="Ngày sinh">
        <b-button class="float-right" style="margin:30px;" @click="create">Thêm sinh viên</b-button>
    </div>    
</template>