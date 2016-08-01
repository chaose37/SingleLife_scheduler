package com.crontab.cvsInfo;

import java.sql.Connection;
import java.sql.PreparedStatement;

import com.crontab.util.ConnectionPool;

public class ConnectionRecipe {
	public static void deleteSingleFood() throws Exception {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = ConnectionPool.getConnection();

			String sql = "delete from sl_recipe";
			
			pstmt = con.prepareStatement(sql);
			pstmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if(pstmt != null) {
				pstmt.close();
			}
			if (con != null) {
				con.close();
			}
		}
	}
	
	public static void insertNaverFood() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//naverFood.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void insertDaumFood() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//daumFood.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
}
