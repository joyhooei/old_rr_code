package com.xiaonei.platform.core.opt.permission.strategy.impl;

import com.xiaonei.platform.core.opt.permission.AbcStrategy;
import com.xiaonei.platform.core.opt.permission.Source;
import com.xiaonei.platform.core.opt.permission.Strategy;
import com.xiaonei.platform.core.opt.permission.impl.RoleImpl;
import com.xiaonei.platform.core.opt.permission.source.Status;
import com.xiaonei.platform.core.opt.permission.strategy.Ret;

public class ConfirmUser extends AbcStrategy {

	public Ret doStrategy(Source guester, Source source) {
		Status visiter = (Status)guester ;
		return RoleImpl.getInstance().isConfirm(visiter)==true?Strategy.RET_TRUE:new Ret(false,false,this.getClassName());
			
	}

}